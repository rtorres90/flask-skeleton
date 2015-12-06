
function detailsAction(test_id){
    detail_row = $("#belongs_to_" + test_id);
    if (detail_row.is(":visible")){
        detail_row.hide(200);
        changeArrowDirection(test_id, "up");
    }else{
        detail_row.show(500);
        changeArrowDirection(test_id, "down");
    }
}

function changeArrowDirection(test_id, direction){
    if (direction == "up"){
        $("#row_down_"+test_id).hide();
        $("#row_up_"+test_id).show();
    }else if(direction == "down"){
        $("#row_down_"+test_id).show();
        $("#row_up_"+test_id).hide();
    }
}
