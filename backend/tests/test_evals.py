"""The offline eval suite runs, and its metrics never fall below the recorded baseline."""

import json

import pytest

from evals import run_evals


@pytest.fixture(scope="module")
def results():
    return run_evals.run()


def test_router_dataset_is_balanced_and_well_formed():
    cases = run_evals.load_jsonl(run_evals.EVAL_DIR / "router_cases.jsonl")

    assert len({c["id"] for c in cases}) == len(cases)
    assert {c["label"] for c in cases} == {"tools", "direct"}
    assert sum(c["label"] == "tools" for c in cases) == len(cases) // 2


def test_binary_metrics():
    m = run_evals.binary_metrics(
        gold=["t", "t", "d", "d"], pred=["t", "d", "t", "d"], positive="t"
    )

    assert m["confusion"] == {"tp": 1, "fp": 1, "fn": 1, "tn": 1}
    assert m["accuracy"] == m["precision"] == m["recall"] == m["f1"] == 0.5


def test_every_routing_failure_is_diagnosed(results):
    router, _ = results

    for failure in router["failures"]:
        assert failure["diagnosis"].startswith(("keyword overlap", "vocabulary gap"))


def test_metrics_do_not_regress_below_baseline(results):
    summary = run_evals.summary_metrics(*results)
    baseline = json.loads(run_evals.BASELINE_PATH.read_text())

    for name, floor in baseline.items():
        assert summary[name] >= floor, f"{name} regressed: {summary[name]} < {floor}"
