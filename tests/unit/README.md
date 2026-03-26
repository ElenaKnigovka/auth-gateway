# Auth Gateway

A lightweight authentication gateway for microservices.

## Features

- JWT-based authentication
- Role-based access control (RBAC)
- OAuth2 integration
- Rate limiting
- Request logging

## Prerequisites

- Node.js 18+
- npm 9+
- Redis (for session storage)

## Installation

```bash
npm install
cp .env.example .env
```

## Configuration

Edit the `.env` file with your configuration:

```ini
PORT=3000
JWT_SECRET=your-secret-key
REDIS_URL=redis://localhost:6379
OAUTH_CLIENT_ID=your-client-id
OAUTH_CLIENT_SECRET=your-client-secret
```

## Usage

Start the server:

```bash
npm start
```

For development with hot-reload:

```bash
npm run dev
```

## API Endpoints

| Method | Path           | Description                |
|--------|----------------|----------------------------|
| POST   | /auth/login    | User login                 |
| POST   | /auth/register | User registration          |
| GET    | /auth/me       | Get current user info      |
| POST   | /auth/refresh  | Refresh access token       |

## Deployment

Build for production:

```bash
npm run build
```

Run in production:

```bash
npm run start:prod
```

## Testing

Run unit tests:

```bash
npm test
```

Run integration tests:

```bash
npm run test:integration
```

## License

MIT