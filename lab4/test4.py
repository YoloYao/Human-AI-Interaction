# Compares similarity value to threshold , if less then google for an answer
if max(cosine_matrix.flatten () ) <= threshold :
    return google_result if ( google_result := google_search ( query ) ) else " I can 't
        find what you are looking for , my liege . Try something else . "