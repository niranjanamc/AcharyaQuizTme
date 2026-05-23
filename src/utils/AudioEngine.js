// A simple procedural audio engine using the Web Audio API
// No external asset downloads required!

class AudioEngine {
  constructor() {
    this.audioCtx = null;
  }

  init() {
    if (!this.audioCtx) {
      this.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (this.audioCtx.state === 'suspended') {
      this.audioCtx.resume();
    }
  }

  playTone(frequency, type, duration, vol = 0.1) {
    if (!this.audioCtx) return;
    const oscillator = this.audioCtx.createOscillator();
    const gainNode = this.audioCtx.createGain();

    oscillator.type = type;
    oscillator.frequency.setValueAtTime(frequency, this.audioCtx.currentTime);
    
    gainNode.gain.setValueAtTime(vol, this.audioCtx.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.001, this.audioCtx.currentTime + duration);

    oscillator.connect(gainNode);
    gainNode.connect(this.audioCtx.destination);

    oscillator.start();
    oscillator.stop(this.audioCtx.currentTime + duration);
  }

  playClick() {
    this.init();
    this.playTone(400, 'sine', 0.1, 0.05);
  }

  playCorrect() {
    this.init();
    // A pleasant ascending arpeggio
    this.playTone(440, 'sine', 0.2, 0.1); // A4
    setTimeout(() => this.playTone(554.37, 'sine', 0.2, 0.1), 100); // C#5
    setTimeout(() => this.playTone(659.25, 'sine', 0.4, 0.1), 200); // E5
  }

  playIncorrect() {
    this.init();
    // A low descending buzz
    this.playTone(300, 'sawtooth', 0.3, 0.05);
    setTimeout(() => this.playTone(250, 'sawtooth', 0.4, 0.05), 150);
  }
  
  playLevelUp() {
    this.init();
    // Triumphant fanfare
    this.playTone(523.25, 'square', 0.15, 0.05); // C5
    setTimeout(() => this.playTone(659.25, 'square', 0.15, 0.05), 150); // E5
    setTimeout(() => this.playTone(783.99, 'square', 0.4, 0.05), 300); // G5
  }
}

export const soundEngine = new AudioEngine();
