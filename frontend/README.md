# Research Compass AI: frontend

React 19 + Vite + Tailwind CSS client for the Research Compass AI backend.
See the [main README](../README.md) for the full project.

```bash
npm install
cp .env.example .env   # VITE_API_URL + Firebase web config for Google sign-in
npm run dev            # http://localhost:5173
npm test               # unit tests (node:test)
npm run lint
npm run build
```

Key folders: `src/pages` (Landing, Dashboard, Chat), `src/components`,
`src/services/api.js` (REST client for the FastAPI backend),
`src/context` (auth and theme providers).
