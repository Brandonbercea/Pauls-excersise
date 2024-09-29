
function fetchExerciseProgram() {
    fetch("http://127.0.0.1:5000/api/v1/exercise?l1=3&l2=1&l3=0")
    .then(response => response.json())
    .then(data => {
        console.log(data);
        displayExerciseProgram(data);
    });
}


function init() {
    $(document).ready(function() {
        fetchExerciseProgram();
    });
}

function bindEvents() {
    const excercises = document.querySelectorAll(".exercise a");
    
    excercises.forEach(link => {
        console.log(link);
        link.addEventListener("click", function(event) {
            event.preventDefault();
            const videoUrl = link.getAttribute("data-video-target");

            if (videoUrl) {
                // fancybox
                $.fancybox.open({
                    src: videoUrl,
                    type: "iframe",
                    iframe: {
                        src: videoUrl,
                        preload: false,
                    }
                });
            }
        });
    });

    $(excercises).fancybox({
        maxWidth    : 800,
        maxHeight   : 600,
        fitToView   : false,
        width       : '70%',
        height      : '70%',
        autoSize    : false,
        closeClick  : false,
        openEffect  : 'none',
        closeEffect : 'none'
    });
}

function displayExerciseProgram(data) {
    buildHtmlForLevel(data.l1, "l1");
    buildHtmlForLevel(data.l2, "l2");
    buildHtmlForLevel(data.l3, "l3");

    bindEvents();
}

function buildHtmlForLevel(levelData, domLevelId) {
    const levelDiv = document.getElementById(domLevelId);
    

    levelDiv.innerHTML = `<h2>Level ${domLevelId}</h2>`;
    
    levelData.forEach((exercise, idx) => {
        levelDiv.innerHTML += `
        <div id="exercise-${idx}" class="exercise">
            <p title="${exercise.notes}">${exercise.name}</p>
            <a href="https://www.youtube.com/embed/lhwT35sshrI?si=K_AA5S4LPBYDgX5u" 
            class="fancybox fancybox.iframe"
            data-fancybox="gallery"
            data-fancybox-type="iframe"
            data-video-target='https://www.youtube.com/embed/lhwT35sshrI?si=K_AA5S4LPBYDgX5u'>${exercise.page}</a>
        </div>`;
    });
}


init();

