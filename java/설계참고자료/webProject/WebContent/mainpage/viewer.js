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
			
			var html ='<div><a href="/webProject/itempage/main.html?name='+alcohol.name+'">'
			html += '<div style="background-image:url(./'+alcohol.img_address+');'
			html += 'height: 270px; width: 200px; background-size:cover "></div>'
			html += '<div width=200px>'
			html +=	'<li>제품명:'+alcohol.name+'</li>'
			html +=	'<li>가격:'+alcohol.price+'</li>'
			html +=	'<li>별점:'+alcohol.star+'</li>'
			html += '</div></a></div>'
			$('#navi ul').last().append(html);
		})
		
		$('#searchbar input').keyup(function(){
			var keyword = $(this).val()
			if(keyword){
				$('#recommend').empty();
				$(data).each(function(index,alcohol){
					
					
					if(keyword==alcohol.name.substr(0,keyword.length)){
						console.log(alcohol.name)
						$('#recommend').css({display:''})
						
						console.log("on")
						
						var html = '<div style="clear:both">'
						html +='<a href="/webProject/itempage/main.html?name='+alcohol.name+'">'
						html +='<div style="background-image:url(./'+alcohol.img_address+');'
						html+= 'height: 90px; width:66px; margin-bottom:5px;background-size:cover;float:left"></div>';
						html += '<div style="height:90px">'
						html +=	'<li>제품명:'+alcohol.name+'</li>'
						html +=	'<li>가격:'+alcohol.price+'</li>'
						html +=	'<li>별점:'+alcohol.star+'</li>'
						html += '</div></a></div>'
						$('#recommend').append(html);
						
					}
				})
				var count = $('#recommend>div').length;
				console.log(count)
				$('#recommend').css({height:count*95});
				if(count==0){
					$('section').css({top:0});
				}else{
					
					$('section').css({top:-count*95-4});
				}
				
			}else{
				
				$('#recommend').css({display:'none'})
				$('section').css({top:''})
				console.log('none')
			}
		})
		
		
	}
	$('.rightButton').click(function(){
		console.log(parseInt($('#navi').css("marginLeft")))
		if(parseInt($('#navi').css("marginLeft"))>-981){
			$('#navi').animate({marginLeft:'-=980'})
		}
	})
	
	$('.leftButton').click(function(){
		if(parseInt($('#navi').css("marginLeft"))<-979){
			$('#navi').animate({marginLeft:'+=980'})
		}
		
	})
	
	

})
	



