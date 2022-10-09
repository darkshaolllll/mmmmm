/<?php
$exp=exp(2);
$pow=pow(4,4);
print($pow."\n");
print($exp."\n");
$number=213123.3422;
print number_format($number);//按照英语的数字写法3个数字一个逗号
print ("\n");
print number_format($number,2,"#","@");
$number=2131.121423423;
list($int,$dec)=explode('.',$number);
print ("\n");
print number_format($number,strlen($dec));
print ("\n");
$number=4;
print "your search returned $number".($number==1?'hit':'hists').'.';
function pc_may_pluralize($singular_word,$amount_of){
    $plurals=array(
        'finsh'=>'fish',
        'person'=>'person',
    );
    if(1==$amount_of){
        return $singular_word;
    }
    if(isset($plurals[$singular_word]))
    {
        return $plurals;
    }
    return $singular_word.'s';
}
$hex='a1';
$decimal=base_convert($hex,16,10);
print ("\n");
print ($decimal);
print ("\n");
print bindec(10101010010);
print ("\n");
print decbin(213);
for($i=0x1;$i<0x10;$i++){
    print dechex($i)."\n";//加了dechex让数字以十六进制的形式输出否则会输出整形
}
?>