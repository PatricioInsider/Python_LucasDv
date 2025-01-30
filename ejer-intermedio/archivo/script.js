// Verificar compatibilidad del navegador para SpeechRecognition
if (!('webkitSpeechRecognition' in window || 'SpeechRecognition' in window)) {
    alert('Tu navegador no soporta reconocimiento de voz. Prueba con Google Chrome.');
} else {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();

    recognition.lang = 'es-ES'; // Configurar el idioma a español
    recognition.interimResults = false; // Obtener solo resultados finales
    recognition.maxAlternatives = 1; // Obtener solo una alternativa

    const listenBtn = document.getElementById('listen-btn');
    const transcript = document.getElementById('transcript');

    recognition.onresult = (event) => {
        const speechToText = event.results[0][0].transcript;
        transcript.textContent = speechToText;
    };

    recognition.onerror = (event) => {
        alert(`Error en el reconocimiento de voz: ${event.error}`);
    };

    listenBtn.addEventListener('click', () => {
        recognition.start();
    });
}

// Funcionalidad de Síntesis de Voz
const speakBtn = document.getElementById('speak-btn');
const textToSpeak = document.getElementById('text-to-speak');

speakBtn.addEventListener('click', () => {
    const speechText = textToSpeak.value;
    if (speechText.trim() !== "") {
        const speechSynthesisUtterance = new SpeechSynthesisUtterance(speechText);
        speechSynthesisUtterance.lang = 'es-ES'; // Configurar el idioma a español
        window.speechSynthesis.speak(speechSynthesisUtterance);
    } else {
        alert('Por favor, escribe algo en el cuadro de texto.');
    }
});
