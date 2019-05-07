$('#insert').click(insert_data);
$('#delete').click(delete_data);
$('#update1').click(update_data);

function insert_data(event){
    event.preventDefault();
    console.log('Insert Data');
    var json_data = { "PropertyName": $('#name').val(),
                     "City": $('#city').val(), 
                     "MarketValue": $('#value').val(), 
                     "Cost": $('#cost').val()};
    console.log(json_data)


    var input_data = JSON.stringify(json_data);
    $.ajax({
        type: 'POST',
        data: json_data,
        url: 'http://localhost:5000/task3_insert',
        success: handleInsertResponse
    });
}

function update_data(event){
    event.preventDefault();
    console.log('update Data');
    var json_data = { "PropertyID" : $('#property_id').val(),
                    "PropertyName": $('#name').val(),
                     "City": $('#city').val(), 
                     "MarketValue": $('#value').val(), 
                     "Cost": $('#cost').val()};

    var input_data = JSON.stringify(json_data);
    $.ajax({
        type: 'POST',
        data: json_data,
        url: 'http://localhost:5000/task3_edit_data',
        success: handleUpdateResponse
    });
}

function delete_data(event){
    event.preventDefault();
	console.log('Delete Data');
    var json_data = { "PropertyID": $('#PropertyID').val()};
    console.log(json_data)
	$.ajax({
        type: 'POST',
        data: json_data,
        url: 'http://localhost:5000/task3_delete',
        success: handleDeleteResponse
    });
}

function handleInsertResponse(data){
	 window.location.reload(true);
}

function handleDeleteResponse(data){
	 window.location.reload(true);
}

function handleUpdateResponse(data){
    console.log('reload web to original web')
    window.location = 'http://localhost:5000/task2'
}


