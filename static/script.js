let appendUserMessage;
let appendBotMessage;

document.addEventListener('DOMContentLoaded', () => {
    const t = document.getElementById('text');
    const searchBtn = document.getElementById('search');
    const voiceBtn = document.getElementById('voice_search');
    const chatArea = document.getElementById('chatArea');
    const modeToggle = document.getElementById('modeToggle');

    document.body.classList.add("light-mode");
    modeToggle.textContent = "☀️";

    modeToggle.addEventListener('click', () => {
        document.body.classList.toggle('light-mode');
        modeToggle.textContent = document.body.classList.contains('light-mode') ? '☀️' : '🌙';

    });

    searchBtn.addEventListener('click', handleSend);
    //SHift enter to go to next line
    t.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    });

    voiceBtn.addEventListener('click', () => {
        voiceBtn.classList.toggle('recording');
    });

    //Get a max height of 4 lines in text box
    const MAX_HEIGHT = 96;
    const MIN_HEIGHT = 24;

    function resizeTextarea() {
        t.style.height = "auto";
        if (t.value.trim() === "") {
            t.style.height = MIN_HEIGHT + "px";
            t.style.overflowY = "hidden";
            return;
        }
        if (t.scrollHeight <= MAX_HEIGHT) {
            t.style.height = t.scrollHeight + "px";
            t.style.overflowY = "hidden";
        } else {
            t.style.height = MAX_HEIGHT + "px";
            t.style.overflowY = "auto";
        }
    }

    t.addEventListener("input", resizeTextarea);

    async function handleSend() {
        const text = t.value.trim();
        if (!text) return;
        appendUserMessage(text);
        t.value = "";
        resizeTextarea();
        const thinkingBubble = appendBotMessage("Thinking...");
        await new Promise(r => setTimeout(r, 10));
        const res = await fetch("/text", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });
        const data = await res.json();
        thinkingBubble.remove();          
        appendBotMessage(data.response); 
    }



    appendUserMessage = function (msg) {
        const d = document.createElement('div');
        d.className = 'itext';
        d.textContent = msg;
        chatArea.appendChild(d);
        chatArea.scrollTop = chatArea.scrollHeight;
        return d;
    }

    appendBotMessage = function (msg) {
        const d = document.createElement('div');
        d.className = 'output';
        d.textContent = msg;
        chatArea.appendChild(d);
        chatArea.scrollTop = chatArea.scrollHeight;
        return d;
    }
});
async function sendText() {
    handleSend();
}

async function sendVoice() {
    const listeningBubble = appendUserMessage("Listening...");
    const res1 = await fetch("/voice", { method: "POST" });
    const data1 = await res1.json();
    listeningBubble.remove();
    appendUserMessage(data1.user);
    const thinkingBubble = appendBotMessage("Thinking...");
    const res2 = await fetch("/text", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: data1.user })
    });
    const data2 = await res2.json();
    thinkingBubble.remove();
    appendBotMessage(data2.response);
}