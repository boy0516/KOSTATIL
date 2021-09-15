$(function(){
	$.ajax({url:"alcohol_list.json", 
		type:"get", 
		dataType:"JSON",
		success:successHandler});
	function successHandler(data){
		console.log(data);
		
		$(data).each(function(index,alcohol){
			console.log((index)%4==0)
			if((index)%4==0){
				var html = '<ul class="view">';
				html +='</ul>'
				$('#navi').append(html);
			}
			
			var html ='<div><div style="background-image:url(./'+alcohol.img_address+');'
			html+= 'height: 270px; width: 200px; background-size:cover "></div>'
			html += '<div width=200px>'+alcohol.name+'</div></div>'
			$('#navi ul').last().append(html);
		})
		
	}
	
})