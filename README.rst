API for OPortfolio
===================

A very simple RESTful API for an open e-portfolio for doctors.

See files in `docs` for details of the endpoints.

Usage
=====

jQuery
++++++

::

    $.ajax({
        url: 'https://o-portfolio-api.herokuapp.com/entries/',
        type: "GET",
        beforeSend: function(xhr) {
            xhr.setRequestHeader("Authorization",
                "basic YWRtaW5AbmhzLmNvbTp0ZXN0"); // Basic HTTP Auth
            },
        success: function(data) {
            console.log("success! " + data);
        },
        error: function(xhr){
            console.log("error :-( " + xhr);
        }
    });

cUrl
++++

::

    curl -v -u users@email.com:password https://o-portfolio-api.herokuapp.com/entries/
