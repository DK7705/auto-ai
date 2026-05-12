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
- Node.js 18+ (for compatibility)
- Python 3.10+ (for ML models)
- MongoDB instance or connection string

## 🔧 Environment Setup

Create a `.env.local` file in `apps/server`:

```env
# Database
DATABASE_URL=mongodb+srv://user:password@cluster.mongodb.net/auto-ai

# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your_anon_key

# API Keys
GOOGLE_API_KEY=your_google_genai_api_key
JWT_SECRET=your_jwt_secret_key

# Server
PORT=3000
NODE_ENV=development
```

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

## 📚 API Routes

### Authentication
- `POST /api/auth/login` — User login
- `POST /api/auth/signup` — User registration

### Models
- `GET /api/models` — List all models
- `POST /api/models` — Create new model
- `GET /api/models/:id` — Get model details
- `PUT /api/models/:id` — Update model
- `DELETE /api/models/:id` — Delete model

### Inference
- `POST /api/inference` — Run model inference
- `GET /api/inference/stats` — Get inference statistics

### Training
- `POST /api/train` — Start model training
- `GET /api/train/:id` — Get training status

### Upload
- `POST /api/upload` — Upload files

## 🐍 Python ML Services

Located in `apps/server/models/`:

```bash
# Install Python dependencies
cd apps/server/models
pip install -r requirements.txt

# Run inference
python run.py --model-path path/to/model --input data.json
```

## 📂 Project Layout

```
auto-ai/
├── apps/
│   ├── server/          # Backend API
│   │   ├── src/
│   │   ├── models/      # Python ML services
│   │   ├── prisma/      # Database schema
│   │   └── package.json
│   ├── web/             # Frontend app
│   │   ├── app/         # Next.js app directory
│   │   ├── components/  # React components
│   │   ├── lib/         # Utilities
│   │   └── package.json
├── package.json         # Root workspace config
└── README.md
```

## 🧪 Available Scripts

- `bun run dev` — Start both server and web concurrently
- `bun run dev:server` — Start backend only
- `bun run dev:web` — Start frontend only
- `bun run db:generate` — Generate Prisma client

## 🔐 Authentication

The app uses Supabase for authentication with JWT tokens. Protected routes require a valid auth token in the `Authorization` header.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues or questions, please open an issue on GitHub.
