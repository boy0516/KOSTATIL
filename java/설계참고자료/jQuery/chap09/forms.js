$(document).ready(function(){
	$('.quantity input').keypress(function(event){
		if(event.which && (event.which < 48 || event.which >57)){
			event.preventDefault();
		}
	}).change(function(){
		var totalQuantity = 0;
		var totalCost = 0;
		
		$('#cart tbody tr').each(function(){
			var price = parseFloat($('.price' , this).text().replace(/^[^\d.]*/, ''));
			price = isNaN(price) ? 0 : price;
			
			var quantity = parseInt($('.quantity input', this).val());
			quantity = isNaN(quantity) ? 0 : quantity;
			
			var cost = price * quantity;
			
			$('.cost', this).text('$' + cost.toFixed(2));
			
		});
		
		
	});
});





