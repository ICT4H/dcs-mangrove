function(doc) {
    var isNotEmpty = function(o) {
        return !((o === undefined) || (o == null) || (o.length == 0));
    };
    if (doc.document_type == 'SurveyResponse' && isNotEmpty(doc.form_model_id) && !doc.void && isNotEmpty(doc.values['tag'])) {
        emit([doc.form_model_id, doc.values['tag'], Date.parse(doc.modified)], doc);
    }
}