from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Record
from .forms import RecordForm

def record_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        records = Record.objects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    else:
        records = Record.objects.all()
    return render(request, 'records/record_list.html', {'records': records})

def record_add(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = RecordForm()
    return render(request, 'records/record_form.html', {'form': form})

def record_edit(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = RecordForm(instance=record)
    return render(request, 'records/record_form.html', {'form': form})

def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(request, 'records/record_confirm_delete.html', {'record': record}) 