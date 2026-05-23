import React, { useEffect, useState } from 'react';

const FloatingAnimation = ({ text, color, onComplete }) => {
  const [position, setPosition] = useState(0);
  const [opacity, setOpacity] = useState(1);

  useEffect(() => {
    const interval = setInterval(() => {
      setPosition(p => p - 2);
      setOpacity(o => o - 0.05);
    }, 50);

    const timeout = setTimeout(() => {
      clearInterval(interval);
      if (onComplete) onComplete();
    }, 1000);

    return () => {
      clearInterval(interval);
      clearTimeout(timeout);
    };
  }, [onComplete]);

  return (
    <div style={{
      position: 'absolute',
      top: `calc(50% + ${position}px)`,
      left: '50%',
      transform: 'translateX(-50%)',
      color: color,
      fontSize: '3rem',
      fontWeight: 'bold',
      opacity: opacity,
      textShadow: '2px 2px 0 #000',
      pointerEvents: 'none',
      zIndex: 100
    }}>
      {text}
    </div>
  );
};

export default FloatingAnimation;
