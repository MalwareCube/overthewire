<?php

$cookie=base64_decode('MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D');
$jsoncookie=json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));

function xor_encrypt($in, $json) {
    $key = $json;
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

print $cookie;
print "\n\n";
print $jsoncookie;
print "\n\nRunning xor_encrypt on cookie\n\n";
print xor_encrypt($cookie, $jsoncookie);
?>
