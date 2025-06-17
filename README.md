# 🎲 Dice Roll Dashboard

A interactive Streamlit dashboard that visualizes probability distributions for dice rolls and coin flips. Teaching probability concepts for kids or just have fun with random number generation.

## 🚀 Features

- Simulate dice rolls (D2, D6, D20, or custom)
- Visualize probability distributions
- Interactive charts showing roll history
- Containerized with Docker for easy deployment

## 🛠️ Prerequisites

- Docker and Docker Compose installed on your system
- Git (for cloning the repository)

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/DiceRollDashboard.git
   cd DiceRollDashboard
   ```

2. **Set up environment variables**
   ```bash
   cp example.env .env
   # Edit .env file if you need to change default settings
   ```

3. **Build and run with Docker Compose**
   ```bash
   docker compose up -d --build
   ```

4. **Access the dashboard**
   - Local: http://localhost:8508
   - Or via your configured domain if using Traefik

## ⚙️ Configuration

Edit the `.env` file to customize:
- `STREAMLIT_SERVER_PORT`: Port to run the Streamlit server (default: 8508)
- `STREAMLIT_SERVER_ADDRESS`: Network interface to bind to (default: 0.0.0.0)
- `TRAEFIK_HOST`: Your domain name if using Traefik

## 🛑 Stopping the Application

```bash
docker compose down
```


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.