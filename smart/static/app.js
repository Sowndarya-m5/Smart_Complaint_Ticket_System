//  UI INTERACTION JS 

// NAVBAR LINK HOVER UNDERLINE EFFECT
document.querySelectorAll(".navbar a").forEach(link => {
    link.addEventListener("mouseenter", () => {
        link.style.borderBottom = "3px solid #ffffff";
        link.style.paddingBottom = "5px";
        link.style.transition = "0.3s";
    });

    link.addEventListener("mouseleave", () => {
        link.style.borderBottom = "none";
    });
});


// BUTTON HOVER COLOR CHANGE
document.querySelectorAll(".btn").forEach(button => {

    const originalBg = window.getComputedStyle(button).backgroundColor;
    const originalColor = window.getComputedStyle(button).color;

    button.addEventListener("mouseenter", () => {
        button.style.backgroundColor = "#0b2c4d";
        button.style.color = "#ffffff";
        button.style.transition = "0.3s";
    });

    button.addEventListener("mouseleave", () => {
        button.style.backgroundColor = originalBg;
        button.style.color = originalColor;
    });
});


// BUTTON CLICK SCALE EFFECT
document.addEventListener("click", function (e) {
    if (e.target.classList.contains("btn")) {
        e.target.style.transform = "scale(0.95)";
        setTimeout(() => {
            e.target.style.transform = "scale(1)";
        }, 150);
    }
});



const words = ["Complaints", "Tickets", "Support", "Requests", "Issues","resolutions","Reports","Queries"];
let i = 0;
const slideshow = document.getElementById("nameslideshow");

function changeWord() {
    slideshow.textContent = words[i];
    i = (i + 1) % words.length;
}

// Change word every 2 seconds
setInterval(changeWord, 1000);

// Initialize
changeWord();




// Toggle chat body open/close
function toggleChat(){
    const box=document.getElementById('chatBox');
    box.style.display = box.style.display==='flex'?'none':'flex';
}

function addMessage(msg,sender){
    const chatBody=document.getElementById('chatBody');
    const div=document.createElement('div');
    div.className='chat-message ' + (sender==='user'?'user-message':'bot-message');
    div.textContent=msg;
    chatBody.appendChild(div);
    chatBody.scrollTop=chatBody.scrollHeight;
}

function sendMessage() {
    const input = document.getElementById('userInput');
    const message = input.value.trim();
    if (message === '') return;

    addMessage(message, 'user');
    input.value = '';

    setTimeout(() => {
        const chatBody = document.getElementById('chatBody');

        if (message.toLowerCase() === 'hi') {
            addMessage('Hi! How can I help you with your complaint?', 'bot');
        } 
        else if (message.toLowerCase().includes('complaint')) {
            addMessage('Press the button below to raise a complaint.', 'bot');

            const button = document.createElement('button');
            button.textContent = 'Click to Add Complaint';
            styleBtn(button);
            button.onclick = () => window.location.href='/complaint';

            appendButton(button);
        } 
        else if (message.toLowerCase().includes('status')) {
            addMessage('Press the button below to check your status.', 'bot');

            const button = document.createElement('button');
            button.textContent = 'Click to Check Status';
            styleBtn(button);
            button.onclick = () => window.location.href='/status';

            appendButton(button);
        } 
        else if (message.toLowerCase().includes('days')) {
            addMessage('Usually, critical problems may take up to 7 working days to be resolved, while minor problems are usually solved within 24 to 48 hours from the date of submission.', 'bot');
        }
        else if (message.toLowerCase().includes('delayed')) {
            addMessage('We`re sorry for the delay🙏. Please check your complaint status using your Ticket ID or contact support.', 'bot');
        }
        else if (message.toLowerCase().includes('thank')) {
            addMessage('You`re welcome😊. If you need any more help, feel free to ask!', 'bot');
        }
        else {
            addMessage("I'm here to assist you with your tickets!", 'bot');
        }

        function appendButton(btn){
            const msgDiv=document.createElement('div');
            msgDiv.className='chat-message bot-message';
            msgDiv.appendChild(btn);
            chatBody.appendChild(msgDiv);
            chatBody.scrollTop=chatBody.scrollHeight;
        }

        function styleBtn(btn){
            btn.style.marginTop='6px';
            btn.style.padding='8px 12px';
            btn.style.background='#e74c3c';
            btn.style.color='white';
            btn.style.border='none';
            btn.style.borderRadius='6px';
            btn.style.cursor='pointer';
        }

    }, 500);
}




// Simple table search (Manager Dashboard)


function searchTable() {
    var input = document.getElementById("searchInput");
    var filter = input.value.toLowerCase();
    var table = document.getElementById("complaintTable");
    var tr = table.getElementsByTagName("tr");

    for (var i = 1; i < tr.length; i++) {
        var txtValue = tr[i].textContent || tr[i].innerText;
        txtValue = txtValue.toLowerCase();

        if (txtValue.indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
    }
}


