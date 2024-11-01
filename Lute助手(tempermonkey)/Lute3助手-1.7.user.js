// ==UserScript==
// @name         Lute3助手
// @namespace    http://tampermonkey.net/
// @version      1.7
// @description  （中文用户）自动填写“原型”，“音标”和“释义”。'ctrl + s'保存单词信息。
// @author       Neo
// @match        http://localhost:*/read/*
// @grant        GM_xmlhttpRequest
// @license      MIT
// @downloadURL https://update.greasyfork.org/scripts/497997/Lute3%E5%8A%A9%E6%89%8B.user.js
// @updateURL https://update.greasyfork.org/scripts/497997/Lute3%E5%8A%A9%E6%89%8B.meta.js
// ==/UserScript==

(function() {
    'use strict';

    autoFulfillForm();

    saveByCtrlPlusS();
})();

// 自动填写单词信息
function autoFulfillForm() {

    // 等待页面加载完成
    window.addEventListener('load', function() {
        let word = document.getElementById('text').value; // 获得单词

        console.log(document.getElementById('translation').value);

        // 使用GM_xmlhttpRequest获取网页内容
        GM_xmlhttpRequest({
            method: 'GET',
            url: `https://www.iciba.com/word?w=${word}`,
            onload: function(response) {
                // 创建一个新的DOM解析器
                const parser = new DOMParser();
                // 将字符串HTML解析为文档对象
                const doc = parser.parseFromString(response.responseText, 'text/html');

                // 获取音标信息
                const phonetics = doc.querySelectorAll('.Mean_symbols__fpCmS li');
                const phoneticTexts = Array.from(phonetics).map(li => li.textContent.trim()).join(', ');

                // 获取释义和词性信息
                const definitions = doc.querySelectorAll('.Mean_part__UI9M6 li');
                const definitionTexts = Array.from(definitions).map(li => {
                    const partOfSpeech = li.querySelector('i') ? li.querySelector('i').textContent.trim() : '';
                    const definition = li.querySelector('div') ? li.querySelector('div').textContent.trim() : '';
                    return `${partOfSpeech} ${definition}`;
                }).join('\n'); // 使用换行符作为分隔

                if(document.getElementById('translation').value == "") {
                    // 填写表单字段
                    console.log(document.getElementById('text').value);
                    let parent = getParent(word, definitionTexts);
                    addParent(parent);// 填写Parents
                    document.getElementById('romanization').value = phoneticTexts; // 填写Pronunciation
                    document.getElementById('translation').value = definitionTexts; // 填写Translation
                    // document.getElementById('status-0').checked = true; // 设置Status为UnKnw
                    // 更多字段填写可以在这里添加
                }

            },
            onerror: function(error) {
                console.error('抓取数据时发生错误:', error);
            }

        });
    }, false);
}

// 添加一个快捷键:'ctrl + s'保存单词
// 已知问题：聚焦到右下角（词典部分）时无法使用快捷键
function saveByCtrlPlusS() {
    window.addEventListener('keydown', function(e) {
        console.log('key is pressed');
        if (e.ctrlKey && e.keyCode == 83) {
            e.preventDefault(); // 阻止's'键的默认行为
            try {
                var iframe = document.getElementById('wordframeid'); // 通过id获取iframe
                var innerDoc = iframe.contentDocument || iframe.contentWindow.document; // 获取iframe的文档对象
                var submitButton = innerDoc.getElementById('submit'); // 从iframe中获取'submit'按钮
                if (submitButton) {
                    submitButton.click(); // 如果找到按钮，则点击它
                }
            } catch (error) {
                console.error('Error accessing the iframe document:', error);
                document.getElementById('submit').click(); // Trigger the submit button click
            }
        }
    }, true); // 使用true来在捕获阶段监听事件


}

// 为单词添加原型(parents)
function addParent(parent) {
    const parentsContainer = document.querySelector('.tagify__input').parentNode;
    let parentTags = Array.from(parentsContainer.querySelectorAll('.tagify__tag')).map(tag => tag.getAttribute('value'));

    // Check if 'parent' is already in 'parentTags', if not, add it
    if (!parentTags.includes(parent)) {
        parentTags.push(parent);

        // Create and insert the new tag
        const tag = document.createElement('tag');
        tag.setAttribute('title', parent);
        tag.setAttribute('contenteditable', 'false');
        tag.setAttribute('spellcheck', 'false');
        tag.setAttribute('tabindex', '-1');
        tag.setAttribute('class', 'tagify__tag');
        tag.setAttribute('value', parent);

        const xButton = document.createElement('x');
        xButton.setAttribute('title', '');
        xButton.setAttribute('class', 'tagify__tag__removeBtn');
        xButton.setAttribute('role', 'button');
        xButton.setAttribute('aria-label', 'remove tag');

        const div = document.createElement('div');
        const span = document.createElement('span');
        span.setAttribute('class', 'tagify__tag-text');
        span.textContent = parent;

        div.appendChild(span);
        tag.appendChild(xButton);
        tag.appendChild(div);

        parentsContainer.insertBefore(tag, parentsContainer.firstChild);

        // Update the hidden input's value
        const hiddenInput = document.getElementById('parentslist');
        hiddenInput.value = JSON.stringify(parentTags.map(tagValue => ({ value: tagValue })));
    }
}

// 从释义中获取单词原型
function getParent(word, definitionTexts) {
    // Use a regular expression to find a pattern of any letters followed by '的'
    const rootFormRegex = /(\b\w+)的/;
    const matches = definitionTexts.match(rootFormRegex);

    // If matches are found, return the first matched group which should be the root form
    if (matches && matches[1]) {
        return matches[1];
    }

    // If no matches are found, return the original word
    return word;
}