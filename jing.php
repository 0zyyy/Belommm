<?php error_reporting(0);
date_default_timezone_set(base64_decode('QXNpYS9KYWthcnRh'));
function postCoday($r0, $c1)
{
    $w2 = curl_init($r0);
    curl_setopt($w2, CURLOPT_POST, true);
    curl_setopt($w2, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($w2, CURLOPT_HTTPHEADER, $c1);
    $c3 = curl_exec($w2);
    curl_close($w2);
    return $c3;
}
function getCoday($r0, $c1)
{
    $w2 = curl_init($r0);
    curl_setopt($w2, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($w2, CURLOPT_HTTPHEADER, $c1);
    $c3 = curl_exec($w2);
    curl_close($w2);
    return $c3;
}
echo base64_decode('PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0K');
echo base64_decode('U0VFRCBBVVRPIENMQUlNICYgQ09NUExFVEUgQUxMIFRBU0sK');
echo base64_decode('Sm9pbiBBaXJEcm9wIEZhbWlseSBJRE4K');
echo base64_decode('aHR0cHM6Ly90Lm1lL0FpcmRyb3BGYW1pbHlJRE4K');
echo base64_decode('PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0K');
echo base64_decode('MS4gQ29tcGxldGUgYWxsIHRhc2sK');
echo base64_decode('Mi4gVXBncmFkZSBUcmVlCg==');
echo base64_decode('My4gVXBncmFkZSBTdG9yYWdlCg==');
echo base64_decode('NC4gQ2hlY2tpbiBEYWlseQo=');
echo base64_decode('PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0K');
$w4 = readline(base64_decode('TWFzdWthbiBQaWxpaGFuIDog'));
$s5 = file(base64_decode('ZGF0YS50eHQ='), FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
foreach ($s5 as $j6 => $j7) {
    $s8 = $j6 + 1;
    $c1 = array(base64_decode('YWNjZXB0OiBhcHBsaWNhdGlvbi9qc29uLCB0ZXh0L3BsYWluLCAqLyo='), base64_decode('b3JpZ2luOiBodHRwczovL2NmLnNlZWRkYW8ub3Jn'), base64_decode('cmVmZXJlcjogaHR0cHM6Ly9jZi5zZWVkZGFvLm9yZy8='), base64_decode('dGVsZWdyYW0tZGF0YTog') . $j7, base64_decode('b3JpZ2luOiBodHRwczovL2NmLnNlZWRkYW8ub3Jn'));
    $n9 = date(base64_decode('ZC1tLVkgSDppOnM='));
    if ($w4 == 1) {
        $o10 = getCoday(base64_decode('aHR0cHM6Ly9zZWVkZGFvLm9yZy9hcGkvdjEvdGFza3MvcHJvZ3Jlc3Nlcw=='), $c1);
        $u11 = json_decode($o10, true);
        $f12 = [];
        foreach ($u11[base64_decode('ZGF0YQ==')] as $y13) {
            $f12[] = $y13[base64_decode('aWQ=')];
        }
        foreach ($f12 as $d14) {
            $n15 = postCoday(base64_decode('aHR0cHM6Ly9zZWVkZGFvLm9yZy9hcGkvdjEvdGFza3Mv') . $d14, $c1);
            $c16 = json_decode($n15, true);
            $r17 = getCoday(base64_decode('aHR0cHM6Ly9zZWVkZGFvLm9yZy9hcGkvdjEvdGFza3Mvbm90aWZpY2F0aW9uLw==') . $c16[base64_decode('ZGF0YQ==')], $c1);
            $l18 = json_decode($r17, true);
            if ($l18[base64_decode('ZGF0YQ==')][base64_decode('ZGF0YQ==')][base64_decode('Y29tcGxldGVk')] == base64_decode('dHJ1ZQ==')) {
                echo "Account $s8 => Reward: " . number_format($l18[base64_decode('ZGF0YQ==')][base64_decode('ZGF0YQ==')][base64_decode('cmV3YXJkX2Ftb3VudA==')] / 1000000000, 6, base64_decode('Lg=='), '') . '' . PHP_EOL;
            } else {
                echo "Account $s8 => $n15" . PHP_EOL;
            }
        }
    } else if ($w4 == 2) {
        $d19 = postCoday(base64_decode('aHR0cHM6Ly9zZWVkZGFvLm9yZy9hcGkvdjEvc2VlZC9taW5pbmctc3BlZWQvdXBncmFkZQ=='), $c1);
        echo "Account $s8 => $d19" . PHP_EOL;
    } else if ($w4 == 3) {
        $d19 = postCoday(base64_decode('aHR0cHM6Ly9zZWVkZGFvLm9yZy9hcGkvdjEvc2VlZC9zdG9yYWdlLXNpemUvdXBncmFkZQ=='), $c1);
        echo "Account $s8 => $d19" . PHP_EOL;
    } else if ($w4 == 4) {
        $x20 = postCoday(base64_decode('aHR0cHM6Ly9zZWVkZGFvLm9yZy9hcGkvdjEvbG9naW4tYm9udXNlcw=='), $c1);
        $l18 = json_decode($x20, true);
        $g21 = $l18[base64_decode('ZGF0YQ==')][base64_decode('bm8=')];
        $a22 = $l18[base64_decode('ZGF0YQ==')][base64_decode('YW1vdW50')];
        if (isset($a22)) {
            echo "Account $s8 => Success Checkin " . $g21 . base64_decode('IFJld2FyZDog') . number_format($a22 / 1000000000, 6, base64_decode('Lg=='), '') . '' . PHP_EOL;
        } else {
            echo "Account $s8 => $x20" . PHP_EOL;
        }
    } else {
        exit();
    }
    echo base64_decode('PT09PT09PT0=') . PHP_EOL;
}
