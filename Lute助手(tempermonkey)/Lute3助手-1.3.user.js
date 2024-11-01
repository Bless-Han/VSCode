// ==UserScript==
// @name         Lute3助手
// @namespace    http://tampermonkey.net/
// @version      1.3
// @description  自动填写“原型”，“音标”和“释义”（中文用户）。
// @author       Neo
// @match        http://localhost:*/read/*
// @grant        GM_xmlhttpRequest
// @license      MIT
// @downloadURL https://update.greasyfork.org/scripts/497997/Lute%E8%87%AA%E5%8A%A8%E5%A1%AB%E5%86%99%E8%AF%8D%E6%B1%87%E4%BF%A1%E6%81%AF.user.js
// @updateURL https://update.greasyfork.org/scripts/497997/Lute%E8%87%AA%E5%8A%A8%E5%A1%AB%E5%86%99%E8%AF%8D%E6%B1%87%E4%BF%A1%E6%81%AF.meta.js
// ==/UserScript==

(function() {
    'use strict';

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
                    document.getElementById('status-0').checked = true; // 设置Status为UnKnw
                    // 更多字段填写可以在这里添加
                }

            },
            onerror: function(error) {
                console.error('抓取数据时发生错误:', error);
            }

        });

    }, false);
})();

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