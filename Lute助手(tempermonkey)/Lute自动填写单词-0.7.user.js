// ==UserScript==
// @name         Lute自动填写单词
// @namespace    http://tampermonkey.net/
// @version      0.7
// @description  Lute3(英语阅读器)辅助工具
// @author       Neo
// @match        http://localhost:9876/*
// @match        https://www.iciba.com/*
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
