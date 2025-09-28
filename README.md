# 🌲 Mystic Forest Flow - Interactive Blockchain Adventure

An interactive text-based adventure game with AI-generated images and Flow blockchain integration. Make choices that shape your destiny and save your story outcomes on the blockchain!

## ✨ Features

- **🎮 Interactive Storytelling**: Choice-based gameplay with branching narratives
- **🎨 AI-Generated Images**: Dynamic images for each scene using Pollinations.ai
- **⛓️ Blockchain Integration**: Save story outcomes on Flow blockchain
- **🏆 Multiple Endings**: Different endings based on your choices and score
- **📱 Responsive Design**: Works on desktop and mobile devices
- **🔗 MetaMask Integration**: Seamless wallet connection and network switching

## 🚀 Live Demo

[Play the Game](https://your-vercel-url.vercel.app) | [View on GitHub](https://github.com/yourusername/mystic-forest-flow)

## 🎯 ETHGlobal Submission

This project is built for **ETHGlobal New Delhi 2025** and targets the **Flow Foundation's $10,000 prize** for gaming applications.

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Ethers.js
- **Backend**: Python Flask
- **Blockchain**: Flow EVM (Ethereum-compatible)
- **Smart Contract**: Solidity
- **Image Generation**: Pollinations.ai API
- **Deployment**: Vercel

## 📋 Prerequisites

- Python 3.7+
- MetaMask wallet
- Flow testnet tokens (for blockchain features)

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mystic-forest-flow.git
   cd mystic-forest-flow
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python -m flask --app api/index.py run
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

### Blockchain Setup

1. **Install MetaMask** browser extension
2. **Add Flow Testnet** to MetaMask:
   - Network Name: Flow
   - RPC URL: `https://testnet.evm.nodes.onflow.org`
   - Chain ID: `545`
   - Currency: FLOW
3. **Get test tokens** from [Flow Testnet Faucet](https://testnet-faucet.onflow.org/)

## 🎮 How to Play

1. **Start your adventure** in the mysterious forest
2. **Make choices** that affect your story path and score
3. **Watch AI-generated images** for each scene
4. **Reach an ending** based on your decisions
5. **Save to blockchain** to permanently store your story
6. **Share your adventure** with friends

## 🏗️ Project Structure

```
mystic-forest-flow/
├── api/
│   └── index.py              # Flask backend server
├── public/
│   ├── index.html            # Main game page
│   ├── script.js             # Frontend JavaScript
│   ├── style.css             # Game styling
│   └── ethers-offline.js     # Offline ethers.js fallback
├── ForestAdventure.sol       # Smart contract
├── forest-adventure.js       # Contract interaction
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel configuration
└── README.md                # This file
```

## 🔧 Smart Contract

The game uses a Solidity smart contract deployed on Flow testnet:

- **Contract Address**: `0xafa6C385c1B6D26Fda55f1a576828B75E9F9FD6c`
- **Functions**: `createStoryOutcome`, `getStoryOutcome`, `getTotalStories`
- **Events**: `StoryCreated`, `StoryUpdated`

### What Gets Stored

Each story outcome includes:
- Story ID and ending category
- Player's final score
- Generated image URLs
- Player's wallet address
- Timestamp

## 🌐 Deployment

### Vercel Deployment

1. **Connect to Vercel**
   - Import your GitHub repository
   - Vercel will auto-detect the Python backend

2. **Environment Variables** (if needed)
   - No environment variables required for basic functionality

3. **Deploy**
   - Vercel will automatically deploy on every push to main branch

### Manual Deployment

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Follow the prompts
```

## 🎯 ETHGlobal Prize Eligibility

This project qualifies for **Flow Foundation's $10,000 prize** because:

- ✅ **Gaming Focus**: Interactive story game fits Flow's ecosystem
- ✅ **Blockchain Integration**: Stories stored on Flow blockchain
- ✅ **User Ownership**: Players own their story outcomes
- ✅ **Innovation**: AI-generated content with blockchain persistence
- ✅ **User Experience**: Seamless MetaMask integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flow Foundation** for the blockchain infrastructure
- **Pollinations.ai** for AI image generation
- **ETHGlobal** for the hackathon platform
- **MetaMask** for wallet integration

## 📞 Support

If you encounter any issues:

1. Check the [Issues](https://github.com/yourusername/mystic-forest-flow/issues) page
2. Create a new issue with detailed description
3. Join the [ETHGlobal Discord](https://discord.gg/ethglobal) for help

---

**Built with ❤️ for ETHGlobal New Delhi 2025**