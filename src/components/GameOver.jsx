import React from 'react';
import { RotateCcw, AlertTriangle, CheckCircle, XCircle, Target } from 'lucide-react';
import { soundEngine } from '../utils/AudioEngine';

const GameOver = ({ score, level, stats, onRestart, language }) => {
  const accuracy = stats.attempted > 0 ? Math.round((stats.correct / stats.attempted) * 100) : 0;

  const labels = {
    title: language === 'kn' ? 'ಅಯ್ಯೋ!' : 'Oh no!',
    subtitle: language === 'kn' ? 'ವಿಮಾನ ಕೆಟ್ಟುಹೋಯಿತು!' : 'The Vimana broke down!',
    finalScore: language === 'kn' ? 'ಅಂತಿಮ ಅಂಕ:' : 'Final Score:',
    reachedLevel: language === 'kn' ? 'ತಲುಪಿದ ಹಂತ:' : 'Reached Level:',
    attempted: language === 'kn' ? 'ಪ್ರಯತ್ನಿಸಿದ ಪ್ರಶ್ನೆಗಳು:' : 'Questions Attempted:',
    correct: language === 'kn' ? 'ಸರಿ:' : 'Correct:',
    wrong: language === 'kn' ? 'ತಪ್ಪು:' : 'Wrong:',
    accuracy: language === 'kn' ? 'ನಿಖರತೆ:' : 'Accuracy:',
    tryAgain: language === 'kn' ? 'ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ' : 'TRY AGAIN'
  };

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100%',
      padding: '20px',
      textAlign: 'center',
      color: 'white',
      backgroundColor: 'rgba(38, 70, 83, 0.8)',
      overflowY: 'auto'
    }}>
      <div style={{
        backgroundColor: 'var(--primary-bg)',
        padding: '30px',
        borderRadius: '20px',
        color: 'var(--text-dark)',
        boxShadow: 'var(--shadow-md)',
        animation: 'slideIn 0.3s ease-out',
        width: '100%',
        maxWidth: '400px'
      }}>
        <AlertTriangle size={64} color="var(--accent-color)" style={{ marginBottom: '10px' }} />
        <h2 style={{ fontSize: '2.5rem', margin: '0 0 10px 0' }}>{labels.title}</h2>
        <p style={{ fontSize: '1.2rem', marginBottom: '20px', fontWeight: 'bold' }}>
          {labels.subtitle}
        </p>
        
        <div style={{ 
          backgroundColor: 'white', 
          padding: '15px', 
          borderRadius: '10px',
          marginBottom: '20px',
          textAlign: 'left'
        }}>
          <h3 style={{ fontSize: '1.5rem', margin: '0 0 10px 0', textAlign: 'center' }}>
            {labels.finalScore} <span style={{ color: 'var(--accent-color)' }}>{score}</span>
          </h3>
          <p style={{ margin: '0 0 10px 0', textAlign: 'center', opacity: 0.8 }}>
            {labels.reachedLevel} {level}
          </p>

          <hr style={{ border: 'none', borderTop: '1px solid #eee', margin: '10px 0' }} />
          
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', fontSize: '0.9rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
               <Target size={16} /> {labels.attempted}
            </div>
            <div style={{ fontWeight: 'bold', textAlign: 'right' }}>{stats.attempted}</div>
            
            <div style={{ display: 'flex', alignItems: 'center', gap: '5px', color: '#06D6A0' }}>
               <CheckCircle size={16} /> {labels.correct}
            </div>
            <div style={{ fontWeight: 'bold', textAlign: 'right', color: '#06D6A0' }}>{stats.correct}</div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '5px', color: 'var(--accent-color)' }}>
               <XCircle size={16} /> {labels.wrong}
            </div>
            <div style={{ fontWeight: 'bold', textAlign: 'right', color: 'var(--accent-color)' }}>{stats.wrong}</div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '5px', marginTop: '5px' }}>
               <span style={{ fontWeight: 'bold' }}>%</span> {labels.accuracy}
            </div>
            <div style={{ fontWeight: 'bold', textAlign: 'right', marginTop: '5px' }}>{accuracy}%</div>
          </div>
        </div>

        <button 
          className="btn btn-secondary" 
          onClick={() => { soundEngine.playClick(); onRestart(); }}
          style={{ width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '10px' }}
        >
          <RotateCcw size={20} /> {labels.tryAgain}
        </button>
      </div>
    </div>
  );
};

export default GameOver;
