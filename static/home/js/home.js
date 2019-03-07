// 顶部轮播图
$(function(){
    var topSwiper = new Swiper('#top-swiper', {
    pagination: '.swiper-pagination',
    slidesPerView: 1,
    paginationClickable: true,
    spaceBetween: 30,
    loop: true,
    autoplay: 4000
    });
});
// 顶部轮播图结束


// 必购js
$(function(){
    var mustbuySwiper = new Swiper('#mustbuy-swiper', {
    slidesPerView: 3,
    spaceBetween: 5,
    loop: true,
    });
});
// 必购js结束

$(function(){
    $('.home').width(innerWidth);
});