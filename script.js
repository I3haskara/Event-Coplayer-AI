// Silent Executive — Enhanced Mock Export Flow

let isProcessing = false;

// --- Helper Functions ---

function logToTerminal(text) {
  const term = document.getElementById('terminal-output');
  if (term) {
    term.innerHTML += `<div>>> ${text}</div>`;
    term.scrollTop = term.scrollHeight; // Auto-scroll
  }
}

// --- The Core Simulation Function ---

function triggerMockExport() {
  if (isProcessing) return; // Prevent double-trigger
  isProcessing = true;
  
  const imageElement = document.getElementById('preview-image');
  const container = document.getElementById('preview-container');

  // 1. Initial State Cleanup
  if (container) container.style.display = 'none';
  const term = document.getElementById('terminal-output');
  if (term) term.innerHTML = ''; // Clear logs

  // 2. THE SIMULATION FLOW
  logToTerminal("EXPORT COMMAND RECOGNIZED: Peace Sign");
  logToTerminal("AUTHENTICATING USER ID: EXEC_01...");
  
  // Auth Delay (0.8s)
  setTimeout(() => {
      logToTerminal("CONNECTION ESTABLISHED: GRAPHON NODE [ACTIVE]");
      logToTerminal("READING LIVE FEED CONTEXT...");
      
      // Reading/Processing Delay (1.5s)
      setTimeout(() => {
          logToTerminal("NANO-BANANA PROTOCOL INITIATED: GENERATING ASSETS...");
          
          // Generation Delay (2.5s) - The main "think" time
          setTimeout(() => {
              
              // THE REVEAL
              logToTerminal("SUCCESS: ASSET SYNCED TO FIGMA [Q3_Audit.fig]");
              logToTerminal("GRAPH STATE SYNCHRONIZED.");
              
              // Set the correct image source and make it visible
              if (imageElement) imageElement.src = './demo_asset_chart.svg'; 
              if (container) container.style.display = 'block'; 
              
              isProcessing = false;
          }, 2500); 
          
      }, 1500); 
      
  }, 800);
}

// --- DEMO TRIGGER (Optional: for testing before gesture integration) ---
// You can call this function manually from your browser's console for testing:
// Example: triggerMockExport();

// Add a floating button to trigger for convenience
(function mountTestButton() {
  function addBtn() {
    if (document.getElementById('mock-export-btn')) return;
    const btn = document.createElement('button');
    btn.id = 'mock-export-btn';
    btn.className = 'btn';
    btn.textContent = '✌️ Run Mock Export';
    btn.style.position = 'fixed';
    btn.style.bottom = '16px';
    btn.style.right = '16px';
    btn.style.zIndex = '9999';
    btn.addEventListener('click', triggerMockExport);
    document.body.appendChild(btn);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addBtn);
  } else {
    addBtn();
  }
})();
