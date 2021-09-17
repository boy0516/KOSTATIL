$(function(){
	$(document).ready(function(){
		console.log(1)
		$.ajax({
			url : 'bestsellerJSON.json',
			type : 'get',
			dataType : 'json',
			success : function(data){
				console.log(2)
				$.each(data,function(index, item){
					var html = '<div class = "product" value =' + ' " ' + item.value + ' " ' +'>';
					html += '<a href = "" class ='+'"'+item.value + '"' + '>';
					html += '<div class = "sumnail">';
					html += '<img class = "product_img" src='+'"'+item.img+'"'+'>'
					html += '</div>';
					html += '<div class = "product_contents">';
					html += '<div class = "contents_wrapper" >';
					html += '<p class = "drink_name">' + item.name + '</p>';
					html += '<div class ="drink_price">'
					html += '<p class = "prev_price">' + item.prevprice + '</p>'
					html += '<p class = "now_price">' + item.nowprice + '</p>'
					html += '</div>';
					html += '<div class "rating_review">';
					html += '<img src = "img/star.png" height = "40px">';
					html += '<p class = "rating Num">' + item.rating + '</p>';
					html += '<p class = "review Num">' + item.review + '</p>';
					html += '</div>';
					html += '</div>';
					html += '</div>';
					html += '</div>';
					html += '</a>';
					html += '</div>';
					console.log(html)
					$('#allProducts').append(html);
					console.log(3)
				});
			}
			
		})
//		$.getJSON('bestsellerJSON.json',function(data){
//				console.log(1)
//			$.each(data,function(index, item){
//				var html = '<div class = "product" value =' + ' " ' + item.value + ' " ' +'>';
//				html += '<a href = "" class ='+'"'+item.value + '"' + '>';
//				html += '<div class = "sumnail">';
//				html += '<img class = "product_img" src='+'"'+item.img+'"'+'>'
//				html += '</div>';
//				html += '<div class = "product_contents">';
//				html += '<div class = "contents_wrapper" >';
//				html += '<p class = "drink_name">' + item.name + '</p>';
//				html += '<div class ="drink_price">'
//				html += '<p class = "prev_price">' + item.prevprice + '</p>'
//				html += '<p class = "now_price">' + item.nowprice + '</p>'
//				html += '</div>';
//				html += '<div class "rating_review">';
//				html += '<img src = "img/star.png" height = "40px">';
//				html += '<p class = "rating num">' + item.rating + '</p>';
//				html += '<p class = "review Num">' + item.review + '</p>';
//				html += '</div>';
//				html += '</div>';
//				html += '</div>';
//				html += '</div>';
//				html += '</a>';
//				html += '</div>';
//				console.log(html)
//				$('#allProducts').append(html);
//				console.log(3)
//			});
//		});
				
			return false;
			
		
		});
	
	$('.drink').click(function(){
		
		$.ajax({
			url : "bestsellerJSON.json",
			type : "get",
			dataType: "JSON",
			success : function(data){
				$.each(data,function(index, item){
					if(data.value == $(this).val()){
					var html = '<div class = "product" value =' + ' " ' + item.value + ' " ' +'>';
					html += '<a href = "" class ='+'"'+item.value + '"' + '>';
					html += '<div class = "sumnail">';
					html += '<img class = "product_img" src='+'"'+item.img+'"'+'>'
					html += '</div>';
					html += '<div class = "product_contents">';
					html += '<div class = "contents_wrapper" >';
					html += '<p class = "drink_name">' + item.name + '</p>';
					html += '<div class ="drink_price">'
					html += '<p class = "prev_price">' + item.prevprice + '</p>'
					html += '<p class = "now_price">' + item.nowprice + '</p>'
					html += '</div>';
					html += '<div class "rating_review">';
					html += '<img src = "img/star.png" height = "40px">';
					html += '<p class = "rating num">' + item.rating + '</p>';
					html += '<p class = "review Num">' + item.review + '</p>';
					html += '</div>';
					html += '</div>';
					html += '</div>';
					html += '</div>';
					html += '</a>';
					html += '</div>';
					console.log(html)
					$('#allProducts').empty()
					$('#allProducts').append(html);
					console.log(3)
					}else{
						return false;
					}
				});
				
					
				
			}
		})
	})
	
//	$('#slider').slider({
//		min : 0,
//		max : 100000,
//		step : 5000,
//		value : 0,
//		slide : function(event, ui){
//			$('#slider').val(ui.value);
//		}
//	});
	
		
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
	
	});
	
	
		
	