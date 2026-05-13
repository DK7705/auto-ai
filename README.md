# Auto-AI

An AI/ML platform for model inference, training, and management with a modern web interface.

## 📋 Project Structure

This is a monorepo containing:

- **`apps/server`** — Express.js backend with tRPC, Prisma ORM, and Python ML integration
- **`apps/web`** — Next.js frontend with React and Supabase authentication
- **`models`** — Python-based ML inference and training services

## 🚀 Tech Stack

### Frontend
- **Next.js** — React framework
- **TypeScript** — Type safety
- **Supabase Auth** — Authentication
- **tRPC** — Type-safe API communication
- **Tailwind CSS** — Styling

### Backend
- **Express.js** — Node.js framework
- **tRPC** — Type-safe RPC
- **Prisma** — ORM for MongoDB
- **Bun** — JavaScript runtime
- **Python** — ML inference and training

### Database & Auth
- **MongoDB** — NoSQL database
- **Supabase** — Authentication provider
- **JWT** — Token-based auth

## 📦 Prerequisites

- [Bun](https://bun.sh) (runtime and package manager)
- [Node.js 18+](https://nodejs.org) (for compatibility)
- [Python 3.13+](https://python.org) (for ML models)
- [uv](https://docs.astral.sh/uv/) (Python project manager — used by the training agent)
- MongoDB instance ([MongoDB Atlas](https://cloud.mongodb.com) free tier works)
- [Supabase](https://supabase.com) project (for GitHub OAuth authentication)
- [Google AI API Key](https://aistudio.google.com/apikey) (for Gemini LLM-powered training)

## 🔧 Credential Setup

> **No secrets are committed to this repo.** You must create your own `.env` files from the provided templates.

### Step 1 — Server Environment

```bash
cp apps/server/.env.example apps/server/.env
```

Edit `apps/server/.env`:

```env
# MongoDB connection string (Atlas or local)
DATABASE_URL=mongodb+srv://<user>:<password>@cluster0.xxxxx.mongodb.net/<dbname>

# Google Gemini API key (from https://aistudio.google.com/apikey)
GOOGLE_API_KEY=your_google_genai_api_key

# Must be your Supabase anon key (used to verify JWTs issued by Supabase)
JWT_SECRET=your_supabase_anon_key

# Server port
PORT=3000
```

### Step 2 — Frontend Environment

```bash
cp apps/web/.env.local.example apps/web/.env.local
```

Edit `apps/web/.env.local`:

```env
# From Supabase Dashboard → Settings → API
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key

# Optional: service role key
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key

# Backend API URL (must match server PORT above)
NEXT_PUBLIC_API_URL=http://localhost:3000
```

### Step 3 — Supabase GitHub OAuth

1. Go to [github.com/settings/developers](https://github.com/settings/developers) → **New OAuth App**
2. Set **Authorization callback URL** to: `https://<your-supabase-ref>.supabase.co/auth/v1/callback`
3. Copy the Client ID and Client Secret
4. In Supabase Dashboard → **Authentication → Providers → GitHub** → enable and paste both values

### Step 4 — MongoDB

1. Create a free cluster on [MongoDB Atlas](https://cloud.mongodb.com)
2. Create a database user
3. Add your IP to the Network Access whitelist (or `0.0.0.0/0` for dev)
4. Copy the connection string into `DATABASE_URL`

## 🎯 Getting Started

### Install Dependencies

```bash
bun install
```

### Generate Prisma Client

```bash
bun run db:generate
```

### Run Development Server

Run everything concurrently:
```bash
bun run dev
```

Or run individually:
```bash
bun run dev:server  # Backend on http://localhost:3000
bun run dev:web     # Frontend on http://localhost:3001
```

## 📚 tRPC API Routes

All routes use tRPC (not REST). Access via `/trpc` endpoint.

| Route | Type | Auth | Description |
|-------|------|------|-------------|
| `stats` | Query | ✅ | Dashboard statistics |
| `models` | Query | ✅ | List user's trained models |
| `upload` | Mutation | ✅ | Upload CSV dataset (base64) |
| `train` | Mutation | ✅ | Start model training from dataset |
| `inference` | Mutation | ✅ | Run prediction on trained model |
| `inferenceHistory` | Query | ✅ | Paginated inference history |
| `getInference` | Query | ✅ | Get specific inference by ID |

## 🐍 Python ML Services

Located in `apps/server/models/`. Python dependencies are managed automatically by `uv` during training.

Manual inference:
```bash
uv run --with joblib --with pandas --with numpy --with scikit-learn \
  python apps/server/models/inference.py <model.joblib> <input.json>
```

## 📂 Project Layout

```
auto-ai/
├── apps/
│   ├── server/              # Express.js + tRPC backend
│   │   ├── src/
│   │   │   ├── routes/      # tRPC route handlers
│   │   │   ├── services/    # Business logic
│   │   │   ├── types/       # TypeScript types & Zod schemas
│   │   │   └── utils/       # JWT, logger helpers
│   │   ├── models/          # Python ML inference scripts
│   │   ├── prisma/          # MongoDB schema
│   │   ├── uploads/         # Uploaded CSV storage (gitignored)
│   │   ├── .env.example     # ← Server env template
│   │   └── package.json
│   └── web/                 # Next.js frontend
│       ├── app/             # App router pages
│       ├── components/      # React + shadcn/ui components
│       ├── hooks/           # Custom React hooks
│       ├── lib/             # Supabase, tRPC, utils
│       ├── .env.local.example # ← Frontend env template
│       └── package.json
├── package.json             # Root workspace config
└── README.md
```

## 🧪 Available Scripts

| Command | Description |
|---------|-------------|
| `bun run dev` | Start both server and web concurrently |
| `bun run dev:server` | Start backend only (port 3000) |
| `bun run dev:web` | Start frontend only (port 3001) |
| `bun run db:generate` | Generate Prisma client from schema |

## 🔐 Authentication

Uses Supabase OAuth (GitHub provider). The flow:
1. User clicks "Continue with GitHub" → redirected to GitHub
2. GitHub redirects back to Supabase → Supabase issues JWT
3. Frontend sends JWT as `Authorization: Bearer <token>` on all tRPC calls
4. Server verifies JWT using the Supabase anon key (`JWT_SECRET`)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues or questions, please open an issue on GitHub.
