function completed(tasks){
    var completed_time = tasks.task.completed_at.value;
    var status = tasks.task.status.value;

    if(status){
    var now = new Date();
       completed_time = now.getDate;
       tasks.task.completed_at = completed_time;
    }
}

function analytics(tasks){

    var start_date = "";
    var end_date = "";

    var created_at = tasks.task.created_at.value;
    var completed_at = tasks.task.completed_at.value;
    var status = tasks.task.status.value;

    if(created_at.get){
        
    }
}