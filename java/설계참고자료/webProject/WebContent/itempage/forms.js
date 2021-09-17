$(function(){
	console.log(1);
	$('.quantity input').change(function(){
		
			var price = parseInt($('table').find('.price').text());
			price = isNaN(price) ? 0 : price;
			
			var quantity = parseInt($('.quantity input').val());
			console.log(quantity)
			quantity = isNaN(quantity) ? 0 : quantity;
			
			var cost = price * quantity;
			$('table tr').find('.cost').text(cost+'\\');
		
	});
});
