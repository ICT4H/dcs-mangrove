class Response(object):
    def __init__(self, reporters=[], submission_id=None, survey_response_id=None, success=False, errors=None,
                 data_record_id=None, short_code=None,
                 cleaned_data=None, is_registration=False, entity_type=None, form_code=None, feed_error_message=None):
        self.reporters = reporters if reporters is not None else []
        self.success = success
        self.survey_response_id = survey_response_id
        self.errors = errors or {}
        self.submission_id = submission_id
        self.datarecord_id = data_record_id
        self.short_code = short_code
        self.processed_data = cleaned_data
        self.is_registration = is_registration
        self.entity_type = entity_type
        self.form_code = form_code
        self.feed_error_message = feed_error_message


def create_response_from_form_submission(reporters, submission_id, form_submission=None):
    if form_submission is not None:
        return Response(reporters, submission_id, None, form_submission.saved, form_submission.errors,
            form_submission.data_record_id,
            form_submission.short_code, form_submission.cleaned_data, form_submission.is_registration,
            form_submission.entity_type,
            form_submission.form_model.form_code)
    return Response(reporters, submission_id)
