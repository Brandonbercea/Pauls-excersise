
function fetchExerciseProgram() {
    fetch("http://127.0.0.1:5000/api/v1/exercise?l1=3&l2=1&l3=0")
    .then(response => response.json())
    .then(data => {
        console.log(data);
        displayExerciseProgram(data);
    });
}


function init() {
    fetchExerciseProgram();
}

function displayExerciseProgram(data) {
    buildHtmlForLevel(data.l1, "l1");
    buildHtmlForLevel(data.l2, "l2");
    buildHtmlForLevel(data.l3, "l3");
}

function buildHtmlForLevel(levelData, domLevelId) {
    const levelDiv = document.getElementById(domLevelId);
    

    levelDiv.innerHTML = `<h2>Level ${domLevelId}</h2>`;
    
    levelData.forEach((exercise, idx) => {
        levelDiv.innerHTML += `
        <div id="exercise-${idx}" class="exercise">
            <p title="${exercise.notes}">${exercise.name}</p>
            <a href="${exercise.page}">${exercise.page}</a>
        </div>`;
    });
}


init();

