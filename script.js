document.addEventListener("DOMContentLoaded", function () {
    const startButton = document.getElementById("start-button");
    startButton.addEventListener("click", startGame);

    function startGame() {
        const characterName = document.getElementById("character-name").value;
        const partnerName = document.getElementById("partner-name").value;

        const gameContainer = document.getElementById("game-container");
        gameContainer.innerHTML = `
            <h1>${characterName}, you meet ${partnerName} at a cafe. Do you smile and say hi? (yes/no)</h1>
            <button id="choice-yes">Yes</button>
            <button id="choice-no">No</button>
        `;

        const choiceYesButton = document.getElementById("choice-yes");
        choiceYesButton.addEventListener("click", showChoiceYes);

        const choiceNoButton = document.getElementById("choice-no");
        choiceNoButton.addEventListener("click", showChoiceNo);
    }

    function showChoiceYes() {
        // Handle "yes" choice here
        // Update the game container accordingly
    }

    function showChoiceNo() {
        // Handle "no" choice here
        // Update the game container accordingly
    }
});
