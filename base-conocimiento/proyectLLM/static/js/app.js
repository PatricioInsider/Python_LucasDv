// ============================================================================
// CHATBOT WEB - JAVASCRIPT
// ============================================================================
// Maneja la comunicación WebSocket, reconocimiento de voz y UI

// ============================================================================
// VARIABLES GLOBALES
// ============================================================================
let socket;
let recognition;
let isListening = false;
let synth = window.speechSynthesis;

// Elementos del DOM
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const btnSend = document.getElementById('btn-send');
const btnVoice = document.getElementById('btn-voice');
const btnClear = document.getElementById('btn-clear');
const typingIndicator = document.getElementById('typing-indicator');
const voiceIndicator = document.getElementById('voice-indicator');
const botName = document.getElementById('bot-name');
const botStatus = document.getElementById('bot-status');

// ============================================================================
// INICIALIZACIÓN
// ============================================================================
document.addEventListener('DOMContentLoaded', () => {
    initializeWebSocket();
    initializeSpeechRecognition();
    initializeEventListeners();
    loadBotInfo();
});

// ============================================================================
// WEBSOCKET
// ============================================================================
function initializeWebSocket() {
    socket = io();

    socket.on('connect', () => {
        console.log('✅ Conectado al servidor');
        updateBotStatus('En línea', true);
    });

    socket.on('disconnect', () => {
        console.log('❌ Desconectado del servidor');
        updateBotStatus('Desconectado', false);
    });

    socket.on('bot_message', (data) => {
        hideTypingIndicator();
        addMessage(data.mensaje, 'bot', data.timestamp);

        // Reproducir respuesta si está habilitado
        speakText(data.mensaje);
    });

    socket.on('history_cleared', () => {
        clearChatMessages();
        showNotification('Historial limpiado');
    });
}

function sendMessage(mensaje) {
    if (!mensaje.trim()) return;

    // Añadir mensaje del usuario
    addMessage(mensaje, 'user');

    // Mostrar indicador de escritura
    showTypingIndicator();

    // Enviar al servidor
    socket.emit('user_message', { mensaje: mensaje });

    // Limpiar input
    userInput.value = '';
}

// ============================================================================
// RECONOCIMIENTO DE VOZ
// ============================================================================
function initializeSpeechRecognition() {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        console.warn('⚠️ Reconocimiento de voz no soportado');
        btnVoice.style.display = 'none';
        return;
    }

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();

    recognition.lang = 'es-ES';
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = () => {
        isListening = true;
        btnVoice.classList.add('active');
        voiceIndicator.style.display = 'block';

        // Cambiar icono
        btnVoice.querySelector('.icon-mic').style.display = 'none';
        btnVoice.querySelector('.icon-mic-off').style.display = 'block';
    };

    recognition.onend = () => {
        isListening = false;
        btnVoice.classList.remove('active');
        voiceIndicator.style.display = 'none';

        // Restaurar icono
        btnVoice.querySelector('.icon-mic').style.display = 'block';
        btnVoice.querySelector('.icon-mic-off').style.display = 'none';
    };

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        console.log('🎤 Reconocido:', transcript);

        userInput.value = transcript;
        sendMessage(transcript);
    };

    recognition.onerror = (event) => {
        console.error('❌ Error de reconocimiento:', event.error);

        if (event.error === 'no-speech') {
            showNotification('No se detectó voz');
        } else if (event.error === 'not-allowed') {
            showNotification('Permiso de micrófono denegado');
        }
    };
}

function toggleVoiceRecognition() {
    if (!recognition) {
        showNotification('Reconocimiento de voz no disponible');
        return;
    }

    if (isListening) {
        recognition.stop();
    } else {
        recognition.start();
    }
}

// ============================================================================
// SÍNTESIS DE VOZ
// ============================================================================
function speakText(text) {
    // Cancelar cualquier síntesis en curso
    synth.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'es-ES';
    utterance.rate = 1.0;
    utterance.pitch = 1.0;

    // Buscar voz en español
    const voices = synth.getVoices();
    const spanishVoice = voices.find(voice => voice.lang.startsWith('es'));
    if (spanishVoice) {
        utterance.voice = spanishVoice;
    }

    synth.speak(utterance);
}

// ============================================================================
// UI - MENSAJES
// ============================================================================
function addMessage(texto, tipo, timestamp) {
    // Remover mensaje de bienvenida si existe
    const welcomeMessage = chatMessages.querySelector('.welcome-message');
    if (welcomeMessage) {
        welcomeMessage.remove();
    }

    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${tipo}`;

    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = tipo === 'user' ? 'TÚ' : '🤖';

    const content = document.createElement('div');
    content.className = 'message-content';

    const bubble = document.createElement('div');
    bubble.className = 'message-bubble';
    bubble.textContent = texto;

    const time = document.createElement('div');
    time.className = 'message-time';
    time.textContent = formatTime(timestamp);

    content.appendChild(bubble);
    content.appendChild(time);

    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);

    chatMessages.appendChild(messageDiv);

    // Scroll al final
    scrollToBottom();
}

function showTypingIndicator() {
    typingIndicator.style.display = 'flex';
    scrollToBottom();
}

function hideTypingIndicator() {
    typingIndicator.style.display = 'none';
}

function clearChatMessages() {
    chatMessages.innerHTML = `
        <div class="welcome-message">
            <div class="welcome-icon">👋</div>
            <h2>¡Bienvenido!</h2>
            <p>Soy tu asistente virtual. Puedes escribir o usar el micrófono para hablar conmigo.</p>
        </div>
    `;
}

function scrollToBottom() {
    chatMessages.parentElement.scrollTop = chatMessages.parentElement.scrollHeight;
}

// ============================================================================
// UI - UTILIDADES
// ============================================================================
function updateBotStatus(status, isOnline) {
    botStatus.textContent = status;
    const statusDot = document.querySelector('.status-dot');

    if (isOnline) {
        statusDot.style.background = '#10b981';
    } else {
        statusDot.style.background = '#ef4444';
    }
}

function showNotification(message) {
    // Crear notificación temporal
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1);
        z-index: 1000;
        animation: slideIn 0.3s ease-out;
    `;
    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

function formatTime(timestamp) {
    if (!timestamp) {
        const now = new Date();
        return now.toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' });
    }

    const date = new Date(timestamp);
    return date.toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' });
}

// ============================================================================
// INFORMACIÓN DEL BOT
// ============================================================================
function loadBotInfo() {
    fetch('/api/info')
        .then(response => response.json())
        .then(data => {
            botName.textContent = data.nombre;
            console.log('🤖 Bot info:', data);
        })
        .catch(error => {
            console.error('Error al cargar info del bot:', error);
        });
}

// ============================================================================
// EVENT LISTENERS
// ============================================================================
function initializeEventListeners() {
    // Enviar mensaje con botón
    btnSend.addEventListener('click', () => {
        sendMessage(userInput.value);
    });

    // Enviar mensaje con Enter
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage(userInput.value);
        }
    });

    // Reconocimiento de voz
    btnVoice.addEventListener('click', toggleVoiceRecognition);

    // Limpiar historial
    btnClear.addEventListener('click', () => {
        if (confirm('¿Estás seguro de que quieres limpiar el historial?')) {
            socket.emit('clear_history');
        }
    });

    // Cargar voces cuando estén disponibles
    if (synth.onvoiceschanged !== undefined) {
        synth.onvoiceschanged = () => {
            synth.getVoices();
        };
    }
}

// ============================================================================
// ANIMACIONES CSS
// ============================================================================
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

console.log('✅ Chatbot Web inicializado');
