import { useState, useEffect } from 'react'
import './index.css'

const AGENTS = [
  '[ORACLE]', '[ARCH]', '[PHIL]', '[ECON]',
  '[PLAN]', '[DATA]', '[DS]', '[ML]', '[SIM]',
  '[QA]', '[RED]', '[SEC]', '[CHAOS]',
  '[SELF]', '[KNOW]', '[DEV]', '[MON]', '[ETH]', '[UX]'
];

const MEMORY_LAYERS = [
  'L1_SENSORY', 'L2_WORKING', 'L3_EPISODIC', 'L4_SEMANTIC',
  'L5_PROCEDURAL', 'L6_EXPERIMENT', 'L7_ERROR', 'L8_OPTIMIZATION',
  'L9_GRAPH', 'L10_COUNTERFACT', 'L11_STRATEGIC', 'L12_COLLECTIVE'
];

const PHASES = [
  { id: 0, title: 'Intent Archaeology', desc: 'Extracting implicit goals + shadow constraints' },
  { id: 1, title: 'World-Model', desc: 'Verifying SOTA research + competitor audit' },
  { id: 2, title: 'System Genesis', desc: 'Designing C4 topology and architecture' },
  { id: 3, title: 'Multi-Agent Execution', desc: 'Coordinate via shared L01-L12 memory' },
  { id: 4, title: 'Adversarial Hardening', desc: 'Attacking, auditing, and chaos testing' },
  { id: 5, title: 'Autonomous Evolution', desc: 'Recursive self-optimization proposals' },
  { id: 6, title: 'Crystallization', desc: 'Emitting PhD-level report + Full Code' }
];

function App() {
  const [intent, setIntent] = useState('');
  const [isExecuting, setIsExecuting] = useState(false);
  const [currentPhase, setCurrentPhase] = useState(-1);
  const [activeAgents, setActiveAgents] = useState([]);
  const [completedPhases, setCompletedPhases] = useState([]);
  const [logs, setLogs] = useState({});
  const [memoryAccess, setMemoryAccess] = useState('');
  const [opsCount, setOpsCount] = useState(0);

  useEffect(() => {
    if(isExecuting) {
      const interval = setInterval(() => {
        setOpsCount(prev => prev + Math.floor(Math.random() * 50) + 10);
      }, 100);
      return () => clearInterval(interval);
    }
  }, [isExecuting]);

  const emulateExecution = async () => {
    if (!intent.trim()) return;
    setIsExecuting(true);
    setCurrentPhase(-1);
    setCompletedPhases([]);
    setLogs({});
    setOpsCount(0);
    
    try {
      fetch('http://localhost:8000/execute', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ intent, constraints: {} })
      }).catch(err => console.error(err));

      for(let i=0; i < PHASES.length; i++) {
        setCurrentPhase(i);
        
        const numAgents = Math.floor(Math.random() * 6) + 3;
        const shuffledA = [...AGENTS].sort(() => 0.5 - Math.random());
        setActiveAgents(shuffledA.slice(0, numAgents));
        
        setMemoryAccess(MEMORY_LAYERS[Math.floor(Math.random() * MEMORY_LAYERS.length)]);
        
        let fullLog = `[SYSTEM] Initializing phase ${i}...\n[NETWORK] Connecting to memory nexus...\n[SUCCESS] Phase ${i} execution complete.`;
        setLogs(prev => ({ ...prev, [i]: '' }));
        
        for (let char of fullLog) {
          setLogs(prev => ({ ...prev, [i]: prev[i] + char }));
          await new Promise(r => setTimeout(r, 10)); 
        }
        
        await new Promise(r => setTimeout(r, 600)); 
        
        setCompletedPhases(c => [...c, i]);
      }
      setActiveAgents([]);
      setMemoryAccess('');
      setIsExecuting(false);
      setCurrentPhase(-1);
    } catch (e) {
      console.error(e);
      setIsExecuting(false);
    }
  };

  return (
    <div className="dashboard-container">
      {/* Header */}
      <div className="header-panel panel">
        <div className="logo-container">
          <div className="logo">
            <span className="logo-icon"></span>
            GENESIS
          </div>
          <div className="logo-sub">Supreme Autonomic Platform</div>
        </div>
        <div className="system-status">
          <div className="status-item">
            <div className="pulse-dot"></div> MAIN LINK
          </div>
          <div className="status-item">
            <div className="pulse-dot" style={{background: '#8b5cf6', boxShadow: '0 0 10px #8b5cf6'}}></div> SECURE KERNEL
          </div>
        </div>
      </div>

      {/* Sidebar Agents */}
      <div className="sidebar-left panel">
        <div className="sidebar-title">COUNCIL_MATRIX</div>
        <div className="agent-grid">
          {AGENTS.map((agent) => {
            const isActive = activeAgents.includes(agent);
            const isCompleted = !isExecuting && completedPhases.length === 7;
            return (
              <div key={agent} className={`agent-badge ${isActive ? 'active' : ''} ${isCompleted ? 'completed' : ''}`}>
                {agent}
              </div>
            )
          })}
        </div>
      </div>

      {/* Main Console */}
      <div className="center-console panel">
        <div className="prompt-panel">
          <div className="terminal-header">
            Enter Execution Directive
          </div>
          <div className="input-group">
            <input 
              type="text" 
              className="input-box"
              placeholder="e.g. Architect a decentralized application..." 
              value={intent}
              onChange={(e) => setIntent(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && emulateExecution()}
              disabled={isExecuting}
            />
            <button className="primary-button" onClick={emulateExecution} disabled={isExecuting || !intent.trim()}>
              {isExecuting ? 'Processing...' : 'Engage'}
            </button>
          </div>
        </div>

        <div className="pipeline-panel">
          <div className="sidebar-title">EXECUTION_PIPELINE</div>
          
          {currentPhase === -1 && completedPhases.length === 0 ? (
            <div className="cyber-loader">
              <div className="spinner"></div>
              <div>System standing by for directives.</div>
            </div>
          ) : (
            <div className="phases-container">
              {PHASES.map((phase) => {
                const isActive = currentPhase === phase.id;
                const isCompleted = completedPhases.includes(phase.id);
                
                return (
                  <div key={phase.id} className={`phase-card ${isActive ? 'active' : ''} ${isCompleted ? 'completed' : ''}`}>
                    <div className="phase-icon">{phase.id + 1}</div>
                    <div className="phase-info">
                      <div className="phase-name">{phase.title}</div>
                      <div className="phase-desc">{phase.desc}</div>
                      {(isActive || isCompleted) && logs[phase.id] && (
                        <div className="log-screen">
                          {logs[phase.id]}
                        </div>
                      )}
                    </div>
                  </div>
                )
              })}
            </div>
          )}
        </div>
      </div>

      {/* Right Sidebar */}
      <div className="sidebar-right panel">
        <div className="sidebar-title">SYSTEM_TELEMETRY</div>
        <div className="stat-grid">
          <div className="stat-box">
            <div className="sidebar-title" style={{marginBottom: '0'}}>Neural Operations</div>
            <div className="stat-value">{opsCount.toLocaleString()}</div>
          </div>
        </div>
        
        <div className="sidebar-title">MEMORY_BANKS</div>
        <div className="memory-layers">
          {MEMORY_LAYERS.map((layer) => (
            <div key={layer} className={`memory-layer ${memoryAccess === layer ? 'active' : ''}`}>
              <span>{layer}</span>
              <span className="layer-status">{memoryAccess === layer ? 'R/W' : 'IDLE'}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default App
