function afterClick(index)
{
		for (var i = 0; i < buttons.length; i++)
		{
			if (i == index)
			{
				buttons[i].id = "buttonAfterClick";
			}
			else
			{
				buttons[i].removeAttribute("id");	
			}
		}
}

var buttons = document.getElementsByClassName("btn btn-default btn-block");

for (var i = 0; i < buttons.length; i++)
{
	let j = i;
	buttons[j].addEventListener("click",function(){
					afterClick(j);	
				}, false);
}