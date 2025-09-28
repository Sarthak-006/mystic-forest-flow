# Flow Blockchain Integration for Mystic Forest Flow

## Overview
This guide shows how to integrate your Mystic Forest Flow game with Flow blockchain to store story outcomes as on-chain data.

## Smart Contract Features

The `ForestAdventure.sol` contract provides:
- **Story Storage**: Store story outcomes with ending category, score, and image URLs
- **Player Tracking**: Track which player created each story
- **Timestamp Recording**: Record when each story was created
- **Image Updates**: Allow players to update their story images

## Setup Instructions

### 1. Deploy the Smart Contract

1. Go to [Remix IDE](https://remix.ethereum.org/)
2. Create a new file called `ForestAdventure.sol`
3. Copy the contract code from `ForestAdventure.sol`
4. Compile the contract (Solidity 0.8.0+)
5. Deploy to Flow Testnet:
   - Connect MetaMask to Flow network
   - Fund your account with Flow tokens from the faucet
   - Deploy the contract
   - Copy the contract address

### 2. Update Your Frontend

Add this to your `public/script.js`:

```javascript
// Add Flow integration
let flowContract = null;
let flowContractAddress = 'YOUR_DEPLOYED_CONTRACT_ADDRESS';

// Initialize Flow contract
async function initFlowContract() {
    if (typeof window.ethereum !== 'undefined') {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const contractABI = [/* Your contract ABI */];
        flowContract = new ethers.Contract(flowContractAddress, contractABI, provider);
    }
}

// Save story to blockchain
async function saveStoryToBlockchain(storyData) {
    if (!flowContract) {
        console.log('Flow contract not initialized');
        return null;
    }

    try {
        const signer = provider.getSigner();
        const contractWithSigner = flowContract.connect(signer);
        
        const tx = await contractWithSigner.createStoryOutcome(
            storyData.endingCategory,
            storyData.score,
            storyData.imageUrl,
            storyData.mangaImageUrl
        );
        
        const receipt = await tx.wait();
        const event = receipt.events.find(e => e.event === 'StoryCreated');
        const storyId = event.args.storyId;
        
        console.log('Story saved to blockchain with ID:', storyId.toString());
        return storyId;
    } catch (error) {
        console.error('Error saving to blockchain:', error);
        return null;
    }
}
```

### 3. Modify Your Game Logic

Update the `displayEndScreen` function in `script.js`:

```javascript
function displayEndScreen(data) {
    // ... existing code ...
    
    // Add blockchain save button
    const saveToBlockchainButton = document.createElement('button');
    saveToBlockchainButton.textContent = 'Save Story to Blockchain';
    saveToBlockchainButton.className = 'reset-button blockchain-button';
    saveToBlockchainButton.addEventListener('click', async () => {
        const storyData = {
            endingCategory: data.ending_category,
            score: data.current_score || data.score,
            imageUrl: data.image_url,
            mangaImageUrl: data.manga_image_url
        };
        
        const storyId = await saveStoryToBlockchain(storyData);
        if (storyId) {
            alert(`Story saved to blockchain with ID: ${storyId}`);
        }
    });
    
    resetContainer.appendChild(saveToBlockchainButton);
    // ... rest of existing code ...
}
```

## Flow Network Configuration

### Add Flow to MetaMask
1. Network Name: Flow Testnet
2. RPC URL: https://testnet.evm.nodes.onflow.org
3. Chain ID: 545
4. Currency Symbol: FLOW

### Get Testnet Tokens
Visit the [Flow Testnet Faucet](https://testnet-faucet.onflow.org/) to get free FLOW tokens for testing.

## Benefits for ETHGlobal Submission

This integration makes your project competitive for Flow's $10,000 prize because:

1. **Gaming Focus**: Perfect fit for Flow's gaming ecosystem
2. **NFT Potential**: Story outcomes can become tradeable NFTs
3. **User Ownership**: Players own their story data on-chain
4. **Social Features**: Enables sharing and trading of story outcomes
5. **Decentralized Storage**: Reduces dependency on centralized services

## Next Steps

1. Deploy the contract to Flow Testnet
2. Integrate the JavaScript functions into your game
3. Test the complete flow
4. Consider adding NFT functionality for story outcomes
5. Add a marketplace for trading story results

## Contract Address
Update the `contractAddress` in `forest-adventure.js` with your deployed contract address after deployment.
