//We get the form and the add task button
var taskForm = document.querySelector(".new-task");
var addTaskButton = document.querySelector("#addTask");
var taskFormOpen = false;
var allTasksLi = document.querySelectorAll(".task-section li span");
//This is for our task info modal view
var modal = document.getElementById("infoModal");
var span = document.getElementsByClassName("close")[0];
var taskTitle = document.getElementById("task-title");
var taskDue = document.getElementById("task-due-date");
var taskDescription = document.getElementById("task-description"); 
//We check if the buttons been clicked and if so then we show the form
//And we close the form if its open and we clicked the button
addTaskButton.addEventListener("click", function () {
    if (taskFormOpen) {
        taskForm.style.display = "none";
        taskFormOpen = false;
    } else {
        taskForm.style.display = "block";
        taskFormOpen = true;
    }
})
span.onclick = function(){
    modal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == modal){
        modal.style.display = "none";
    }
}
function addTaskInfo(taskList){
    for (const task of allTasksLi) {
    task.addEventListener("click", function () {
        var taskObj = taskList[task.getAttribute("value")];
        taskTitle.innerText = taskObj["title"];
        taskDue.innerText = "Due: "+taskObj["due date"]
        taskDescription.innerText = taskObj["description"]
        modal.style.display = "block"
    })
}
}
