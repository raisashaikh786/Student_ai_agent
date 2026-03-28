const BASE_URL = "http://127.0.0.1:8000";

// TASKS
async function addTask() {
    let task = document.getElementById("taskInput").value;

    await fetch(BASE_URL + "/add-task", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            title: task,
            deadline: "tomorrow",
            priority: 1
        })
    });

    document.getElementById("taskInput").value = "";
    loadTasks();
}

async function loadTasks() {
    let res = await fetch(BASE_URL + "/tasks");
    let data = await res.json();

    let list = document.getElementById("taskList");
    list.innerHTML = "";

    data.forEach(t => {
        let li = document.createElement("li");
        li.innerText = `${t.title} (Priority: ${t.priority})`;
        list.appendChild(li);
    });
}

// PLANNER
async function loadPlan() {
    let res = await fetch(BASE_URL + "/plan");
    let data = await res.json();

    let list = document.getElementById("planList");
    list.innerHTML = "";

    data.schedule.forEach(item => {
        let li = document.createElement("li");
        li.innerText = `${item.time} → ${item.task}`;
        list.appendChild(li);
    });
}

// CHAT
async function sendMessage() {
    showLoader();

    let question = document.getElementById("chatInput").value;

    let res = await fetch(BASE_URL + "/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question})
    });

    let data = await res.json();
    document.getElementById("chatResponse").innerText = data.answer;

    hideLoader();
}

// NOTES
async function summarize() {
    let text = document.getElementById("noteInput").value;

    let res = await fetch(BASE_URL + "/summarize", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text})
    });

    let data = await res.json();
    document.getElementById("summary").innerText = data.summary;
}
// FOCUS
async function getFocus() {
    let res = await fetch(BASE_URL + "/focus-score");
    let data = await res.json();

    document.getElementById("focusResult").innerText =
        `Score: ${data.score} - ${data.message}`;
}

// WARNINGS
async function getWarnings() {
    let res = await fetch(BASE_URL + "/warnings");
    let data = await res.json();

    let list = document.getElementById("warningsList");
    list.innerHTML = "";

    data.warnings.forEach(w => {
        let li = document.createElement("li");
        li.innerText = w;
        list.appendChild(li);
    });
}

function showLoader() {
    document.getElementById("loader").style.display = "block";
}

function hideLoader() {
    document.getElementById("loader").style.display = "none";
}

function setGreeting() {
    let hour = new Date().getHours();
    let msg = "Hello 👋";

    if (hour < 12) msg = "🌅 Good Morning";
    else if (hour < 18) msg = "☀️ Good Afternoon";
    else msg = "🌙 Good Evening";

    document.getElementById("greeting").innerText = msg + ", Student!";
}

setGreeting();
// AUTO LOAD
loadTasks();