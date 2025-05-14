// 投票系统交互脚本

document.addEventListener('DOMContentLoaded', function() {
  // 选项交互增强
  const choiceItems = document.querySelectorAll('.choice-item');
  
  choiceItems.forEach(item => {
    // 点击整个选项区域时选中对应的单选按钮
    item.addEventListener('click', function(e) {
      // 避免点击单选按钮本身时触发两次
      if (e.target.tagName !== 'INPUT') {
        const radio = item.querySelector('input[type="radio"]');
        radio.checked = true;
      }
    });
  });
});