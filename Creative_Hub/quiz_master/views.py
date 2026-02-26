from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Answer

def index(request):
    quizzes = Quiz.objects.all().order_by('-created_at')
    return render(request, 'quiz_master/index.html', {'quizzes': quizzes})

def take_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all().prefetch_related('answers')
    if request.method == 'POST':
        score = 0
        results = []
        for q in questions:
            selected_id = request.POST.get(f'q_{q.id}')
            correct = q.answers.filter(is_correct=True).first()
            selected = Answer.objects.filter(pk=selected_id).first() if selected_id else None
            is_correct = selected and selected.is_correct
            if is_correct:
                score += 1
            results.append({'question': q, 'selected': selected, 'correct': correct, 'is_correct': is_correct})
        return render(request, 'quiz_master/results.html', {
            'quiz': quiz, 'results': results, 'score': score, 'total': questions.count()
        })
    return render(request, 'quiz_master/take.html', {'quiz': quiz, 'questions': questions})
