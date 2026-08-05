import test from "node:test";
import assert from "node:assert/strict";

import { shouldProcessInitialQuery } from "./initialQueryGuard.js";

test("processes the first navigation for a given location key and ignores repeats", () => {
  const seenKeys = new Set();

  assert.equal(shouldProcessInitialQuery("chat-1", seenKeys), true);
  assert.equal(shouldProcessInitialQuery("chat-1", seenKeys), false);
  assert.equal(shouldProcessInitialQuery("chat-2", seenKeys), true);
});

test("returns false when there is no location key", () => {
  const seenKeys = new Set();

  assert.equal(shouldProcessInitialQuery(undefined, seenKeys), false);
});
