/**
 * 
 */

$(function(){
	$.ajax({url:"alcohol_list.json", 
		type:"get", 
		dataType:"JSON",
		success:successHandler});
	function successHandler(data){
		console.log(data);
		
		
		
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
						html +='<a href="https://www.sooldamhwa.com/damhwaMarket/detail/1051";>'
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
})