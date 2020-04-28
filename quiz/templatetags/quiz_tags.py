from django import template
from core.models import Profile

register = template.Library()


@register.inclusion_tag('correct_answer.html', takes_context=True)
def correct_answer_for_all(context, question):
    """
    processes the correct answer based on a given question object
    if the answer is incorrect, informs the user
    """
    answers = question.get_answers()
    incorrect_list = context.get('incorrect_questions', [])
    if question.id in incorrect_list:
        user_was_incorrect = True
    else:
        user_was_incorrect = False

    return {'previous': {'answers': answers},
            'user_was_incorrect': user_was_incorrect}


@register.filter
def answer_choice_to_string(question, answer):
    return question.answer_choice_to_string(answer)

@register.filter
def base(request):
    try:
        profileData = Profile.objects.get(displayName=request.user)
    except ObjectDoesNotExist:
        profileData = []
        messages.info(request, "Please Create a Profile")
    context = {
        'profileData': profileData,
    }
    return render(context)
    