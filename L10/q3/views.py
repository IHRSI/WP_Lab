from django.shortcuts import redirect, render

from .models import Human


def index(request):
	humans = Human.objects.all().order_by("first_name")
	selected_human = None

	selected_id = request.GET.get("human")
	if selected_id:
		selected_human = Human.objects.filter(id=selected_id).first()

	if request.method == "POST":
		selected_id = request.POST.get("human")
		selected_human = Human.objects.filter(id=selected_id).first()

		if selected_human:
			action = request.POST.get("action")
			if action == "update":
				selected_human.first_name = request.POST.get("first_name", "")
				selected_human.last_name = request.POST.get("last_name", "")
				selected_human.phone = request.POST.get("phone", "")
				selected_human.address = request.POST.get("address", "")
				selected_human.city = request.POST.get("city", "")
				selected_human.save()
				return redirect(f"/q3/?human={selected_human.id}")

			if action == "delete":
				selected_human.delete()
				return redirect("q3_index")

	return render(
		request,
		"q3/index.html",
		{
			"humans": humans,
			"selected_human": selected_human,
		},
	)
