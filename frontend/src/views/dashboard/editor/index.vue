<template>
  <div class="dashboard-editor-container">
    <body for="html-export">
      <div class="mume markdown-preview">
        <div>
          <h1 align="center">Tplan &#x1F44B;</h1>
          <p align="center">
            <img
              src="https://img.shields.io/badge/Python-3.7 | 3.8 | 3.9-blue"
            />
            <img src="https://img.shields.io/badge/license-MIT-green" />
            <img src="https://img.shields.io/badge/Celery-5.0.5-blue" />
            <img src="https://img.shields.io/badge/Arq-0.22-blue" />
            <img src="https://img.shields.io/badge/Fastapi-0.4.9-red" />
            <img src="https://img.shields.io/badge/uvicorn-0.2.2-yellow" />
            <img
              src="https://img.shields.io/badge/pydantic-0.2.2-brightgreen"
            />
            <img src="https://img.shields.io/badge/fabric-0.1.13-yellow" />
            <img
              src="https://img.shields.io/badge/pydantic-0.2.2-brightgreen"
            />
            <img src="https://img.shields.io/badge/Mysql-5.7-yellow" />
            <img src="https://img.shields.io/badge/paramiko-latest-yellow" />
            <img src="https://img.shields.io/badge/Vue-2.0-brightgreen" />
          </p>
      

          <h2 class="mume-header" id="%E5%85%B3%E4%BA%8Etplan">
            &#x1F44A; &#x5173;&#x4E8E;<code>Tplan</code>
          </h2>

          <ul>
            <li>
              &#x1F603; <code>T&#x8BA1;&#x5212;</code>
              &#x662F;&#x4E00;&#x4E2A;&#x96C6;&#x6210;&#x4E86;<code>&#x4EFB;&#x52A1;&#x961F;&#x5217;</code>&#x3001;<code>&#x8FDB;&#x7A0B;&#x7BA1;&#x7406;</code>&#x3001;<code>&#x722C;&#x866B;&#x90E8;&#x7F72;</code>&#x3001;<code>&#x670D;&#x52A1;&#x53EF;&#x89C6;&#x5316;&#x76D1;&#x63A7;</code>&#x3001;<code>&#x6570;&#x636E;&#x5C55;&#x793A;</code>&#x3001;<code>&#x5728;&#x7EBF;&#x7F16;&#x7801;</code>&#x3001;<code>&#x8FDC;&#x7A0B;&#x90E8;&#x7F72;</code>&#x7684;&#x901A;&#x7528;&#x7CFB;&#x7EDF;
            </li>
            <li>
              &#x1F528; &#x540E;&#x7AEF;&#x670D;&#x52A1;&#x91C7;&#x7528;&#x4E86;
              <code>fastapi</code>
              &#x6846;&#x67B6;&#xFF0C;&#x642D;&#x914D;&#x4E86;
              <code>Mysql</code
              >&#x3001;<code>Mongodb</code>&#x3001;<code>Redis&#x7F13;&#x5B58;</code>&#x3002;&#x524D;&#x7AEF;&#x91C7;&#x7528;
              <code>Vue</code> &#x6846;&#x67B6;&#x548C;
              <code>elementui</code> &#x5F00;&#x6E90;&#x7EC4;&#x4EF6;
            </li>
            <li>
              &#x1F44A;
              &#x70ED;&#x5207;&#x7684;&#x5E0C;&#x671B;&#x8BE5;&#x9879;&#x76EE;&#x80FD;&#x80DC;&#x4EFB;&#x65E5;&#x5E38;&#x7684;&#x8FD0;&#x7EF4;&#x7BA1;&#x7406;&#x5DE5;&#x4F5C;
            </li>
            <li>
              &#x1F6A5;
              &#x6211;&#x53EF;&#x80FD;&#x9700;&#x8981;&#x66F4;&#x591A;&#x7684;&#x7075;&#x611F;&#x548C;&#x5EFA;&#x8BAE;&#x3001;&#x5982;&#x679C;&#x60A8;&#x6709;&#x66F4;&#x597D;&#x7684;&#x60F3;&#x6CD5;&#xFF0C;&#x8BF7;&#x8054;&#x7CFB;&#x6211;
              &#x1F64C;&#x1F64C;
            </li>
            <li>
              &#x274C;
              &#x6700;&#x540E;&#x975E;&#x5E38;&#x538C;&#x5026;&#x90A3;&#x4E9B;&#x9879;&#x76EE;&#x95ED;&#x6E90;&#x800C;&#x53C8;&#x4E0D;&#x613F;&#x5206;&#x6790;&#x6280;&#x672F;&#x5B9E;&#x73B0;&#x3001;&#x54EA;&#x6015;&#x662F;&#x4E00;&#x70B9;&#x70B9;&#x601D;&#x8DEF;&#x7684;&#x4EBA;
            </li>
          </ul>
      

          <h2 class="mume-header" id="%E5%B7%B2%E5%AE%8C%E6%88%90">
            &#x1F389; &#x5DF2;&#x5B8C;&#x6210;
          </h2>

          <ul>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" checked />
              &#x767B;&#x5F55;/&#x6CE8;&#x9500;
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" checked />
              &#x7528;&#x6237;&#x6743;&#x9650;&#x7BA1;&#x7406;
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" checked />
              &#x6570;&#x636E;&#x5C55;&#x793A;
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" checked />
              &#x65B0;&#x589E;&#x8282;&#x70B9;&#x3001;&#x6D4B;&#x8BD5;&#x8282;&#x70B9;
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" checked />
              &#x8282;&#x70B9;&#x7BA1;&#x7406;
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" checked />
              <code>&#x8FDC;&#x7A0B;&#x7F16;&#x7801;</code>
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" checked />
              <code>Prometheus</code>
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" checked />
              <code>Celery</code>
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" checked />
              <code>Docker</code>
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" checked />
              <code>Supervisor</code>
            </li>
          </ul>
          <h2 class="mume-header" id="%E5%BE%85%E5%8A%9E">
            &#x1F44B; &#x5F85;&#x529E;
          </h2>

          <ul>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" />
              &#x722C;&#x866B;&#x4EFB;&#x52A1;
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" />
              &#x8FDC;&#x7A0B;&#x6279;&#x91CF;&#x90E8;&#x7F72;&#x548C;&#x8C03;&#x5EA6;
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" />
              &#x524D;&#x7AEF;&#x65E5;&#x5FD7;&#x5C55;&#x793A;
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" />
              &#x4EFB;&#x52A1;&#x544A;&#x8B66;
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" />
              <code>WebSocket</code>
              &#x4EFB;&#x52A1;&#x65E5;&#x5FD7;&#x3001;&#x8282;&#x70B9;&#x65E5;&#x5FD7;
            </li>
            <li class="task-list-item">
              <input type="checkbox" class="task-list-item-checkbox" />
              <code>Arq</code> &#x961F;&#x5217;
            </li>
          </ul>
   
          <h2 class="mume-header" id="pr">&#x1F50B; PR</h2>

          <blockquote>
            <p>
              &#x6211;&#x5F53;&#x7136;&#x5E0C;&#x671B;&#x4F60;&#x80FD;&#x591F;&#x6709;&#x66F4;&#x597D;&#x7684;&#x60F3;&#x6CD5;&#x6216;&#x8D21;&#x732E;&#x3002;
            </p>
          </blockquote>
          <h2 class="mume-header" id="%E7%89%B9%E5%88%AB%E9%B8%A3%E8%B0%A2">
            &#x1F449; &#x7279;&#x522B;&#x9E23;&#x8C22;
          </h2>

          <ul>
            <li>
              &#x611F;&#x8C22;
              <a href="https://github.com/PanJiaChen">PanJiaChen</a>
              &#x5F00;&#x6E90;&#x7684;&#x524D;&#x7AEF;&#x9879;&#x76EE;
              <a href="https://github.com/PanJiaChen/vue-element-admin"
                >https://github.com/PanJiaChen/vue-element-admin</a
              >
            </li>
            <li>
              &#x611F;&#x8C22;
              <a href="https://github.com/samuelcolvin/arq">Arq</a> &#x548C;
              <a href="https://github.com/tiangolo/fastapi">FastAPI</a>
            </li>
          </ul>
          <h2 class="mume-header" id="%E5%BC%80%E6%BA%90%E8%AE%B8%E5%8F%AF">
            &#x1F4DD; &#x5F00;&#x6E90;&#x8BB8;&#x53EF;
          </h2>
           <a href="#">MIT</a>

        </div>
      </div>
    </body>
  </div>
</template>


<style scoped>

code[class*="language-"],
pre[class*="language-"] {
  color: #333;
  background: none;
  font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
  text-align: left;
  white-space: pre;
  word-spacing: normal;
  word-break: normal;
  word-wrap: normal;
  line-height: 1.4;

  -moz-tab-size: 8;
  -o-tab-size: 8;
  tab-size: 8;

  -webkit-hyphens: none;
  -moz-hyphens: none;
  -ms-hyphens: none;
  hyphens: none;
}

/* Code blocks */
pre[class*="language-"] {
  padding: 0.8em;
  overflow: auto;
  /* border: 1px solid #ddd; */
  border-radius: 3px;
  /* background: #fff; */
  background: #f5f5f5;
}

/* Inline code */
:not(pre) > code[class*="language-"] {
  padding: 0.1em;
  border-radius: 0.3em;
  white-space: normal;
  background: #f5f5f5;
}

.token.comment,
.token.blockquote {
  color: #969896;
}

.token.cdata {
  color: #183691;
}

.token.doctype,
.token.punctuation,
.token.variable,
.token.macro.property {
  color: #333;
}

.token.operator,
.token.important,
.token.keyword,
.token.rule,
.token.builtin {
  color: #a71d5d;
}

.token.string,
.token.url,
.token.regex,
.token.attr-value {
  color: #183691;
}

.token.property,
.token.number,
.token.boolean,
.token.entity,
.token.atrule,
.token.constant,
.token.symbol,
.token.command,
.token.code {
  color: #0086b3;
}

.token.tag,
.token.selector,
.token.prolog {
  color: #63a35c;
}

.token.function,
.token.namespace,
.token.pseudo-element,
.token.class,
.token.class-name,
.token.pseudo-class,
.token.id,
.token.url-reference .token.variable,
.token.attr-name {
  color: #795da3;
}

.token.entity {
  cursor: help;
}

.token.title,
.token.title .token.punctuation {
  font-weight: bold;
  color: #1d3e81;
}

.token.list {
  color: #ed6a43;
}

.token.inserted {
  background-color: #eaffea;
  color: #55a532;
}

.token.deleted {
  background-color: #ffecec;
  color: #bd2c00;
}

.token.bold {
  font-weight: bold;
}

.token.italic {
  font-style: italic;
}

/* JSON */
.language-json .token.property {
  color: #183691;
}

.language-markup .token.tag .token.punctuation {
  color: #333;
}

/* CSS */
code.language-css,
.language-css .token.function {
  color: #0086b3;
}

/* YAML */
.language-yaml .token.atrule {
  color: #63a35c;
}

code.language-yaml {
  color: #183691;
}

/* Ruby */
.language-ruby .token.function {
  color: #333;
}

/* Markdown */
.language-markdown .token.url {
  color: #795da3;
}

/* Makefile */
.language-makefile .token.symbol {
  color: #795da3;
}

.language-makefile .token.variable {
  color: #183691;
}

.language-makefile .token.builtin {
  color: #0086b3;
}

/* Bash */
.language-bash .token.keyword {
  color: #0086b3;
}

/* highlight */
pre[data-line] {
  position: relative;
  padding: 1em 0 1em 3em;
}

pre[data-line] .line-highlight-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  background-color: transparent;
  display: block;
  width: 100%;
}

pre[data-line] .line-highlight {
  position: absolute;
  left: 0;
  right: 0;
  padding: inherit 0;
  margin-top: 1em;
  background: hsla(24, 20%, 50%, 0.08);
  background: linear-gradient(
    to right,
    hsla(24, 20%, 50%, 0.1) 70%,
    hsla(24, 20%, 50%, 0)
  );
  pointer-events: none;
  line-height: inherit;
  white-space: pre;
}

pre[data-line] .line-highlight:before,
pre[data-line] .line-highlight[data-end]:after {
  content: attr(data-start);
  position: absolute;
  top: 0.4em;
  left: 0.6em;
  min-width: 1em;
  padding: 0 0.5em;
  background-color: hsla(24, 20%, 50%, 0.4);
  color: hsl(24, 20%, 95%);
  font: bold 65%/1.5 sans-serif;
  text-align: center;
  vertical-align: 0.3em;
  border-radius: 999px;
  text-shadow: none;
  box-shadow: 0 1px white;
}

pre[data-line] .line-highlight[data-end]:after {
  content: attr(data-end);
  top: auto;
  bottom: 0.4em;
}

html body {
  font-family: "Helvetica Neue", Helvetica, "Segoe UI", Arial, freesans,
    sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #333;
  background-color: #fff;
  overflow: initial;
  box-sizing: border-box;
  word-wrap: break-word;
}

html body > :first-child {
  margin-top: 0;
}

html body h1,
html body h2,
html body h3,
html body h4,
html body h5,
html body h6 {
  line-height: 1.2;
  margin-top: 1em;
  margin-bottom: 16px;
  color: #000;
}

html body h1 {
  font-size: 2.25em;
  font-weight: 300;
  padding-bottom: 0.3em;
}

html body h2 {
  font-size: 1.75em;
  font-weight: 400;
  padding-bottom: 0.3em;
}

html body h3 {
  font-size: 1.5em;
  font-weight: 500;
}

html body h4 {
  font-size: 1.25em;
  font-weight: 600;
}

html body h5 {
  font-size: 1.1em;
  font-weight: 600;
}

html body h6 {
  font-size: 1em;
  font-weight: 600;
}

html body h1,
html body h2,
html body h3,
html body h4,
html body h5 {
  font-weight: 600;
}

html body h5 {
  font-size: 1em;
}

html body h6 {
  color: #5c5c5c;
}

html body strong {
  color: #000;
}

html body del {
  color: #5c5c5c;
}

html body a:not([href]) {
  color: inherit;
  text-decoration: none;
}

html body a {
  color: #08c;
  text-decoration: none;
}

html body a:hover {
  color: #00a3f5;
  text-decoration: none;
}

html body img {
  max-width: 100%;
}

html body > p {
  margin-top: 0;
  margin-bottom: 16px;
  word-wrap: break-word;
}

html body > ul,
html body > ol {
  margin-bottom: 16px;
}

html body ul,
html body ol {
  padding-left: 2em;
}

html body ul.no-list,
html body ol.no-list {
  padding: 0;
  list-style-type: none;
}

html body ul ul,
html body ul ol,
html body ol ol,
html body ol ul {
  margin-top: 0;
  margin-bottom: 0;
}

html body li {
  margin-bottom: 0;
}

html body li.task-list-item {
  list-style: none;
}

html body li > p {
  margin-top: 0;
  margin-bottom: 0;
}

html body .task-list-item-checkbox {
  margin: 0 0.2em 0.25em -1.8em;
  vertical-align: middle;
}

html body .task-list-item-checkbox:hover {
  cursor: pointer;
}

html body blockquote {
  margin: 16px 0;
  font-size: inherit;
  padding: 0 15px;
  color: #5c5c5c;
  background-color: #f0f0f0;
  border-left: 4px solid #d6d6d6;
}

html body blockquote > :first-child {
  margin-top: 0;
}

html body blockquote > :last-child {
  margin-bottom: 0;
}

html body hr {
  height: 4px;
  margin: 32px 0;
  background-color: #d6d6d6;
  border: 0 none;
}

html body table {
  margin: 10px 0 15px 0;
  border-collapse: collapse;
  border-spacing: 0;
  display: block;
  width: 100%;
  overflow: auto;
  word-break: normal;
  word-break: keep-all;
}

html body table th {
  font-weight: bold;
  color: #000;
}

html body table td,
html body table th {
  border: 1px solid #d6d6d6;
  padding: 6px 13px;
}

html body dl {
  padding: 0;
}

html body dl dt {
  padding: 0;
  margin-top: 16px;
  font-size: 1em;
  font-style: italic;
  font-weight: bold;
}

html body dl dd {
  padding: 0 16px;
  margin-bottom: 16px;
}

html body code {
  font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
  font-size: 0.85em !important;
  color: #000;
  background-color: #f0f0f0;
  border-radius: 3px;
  padding: 0.2em 0;
}

html body code::before,
html body code::after {
  letter-spacing: -0.2em;
  content: "\00a0";
}

html body pre > code {
  padding: 0;
  margin: 0;
  font-size: 0.85em !important;
  word-break: normal;
  white-space: pre;
  background: transparent;
  border: 0;
}

html body .highlight {
  margin-bottom: 16px;
}

html body .highlight pre,
html body pre {
  padding: 1em;
  overflow: auto;
  font-size: 0.85em !important;
  line-height: 1.45;
  border: #d6d6d6;
  border-radius: 3px;
}

html body .highlight pre {
  margin-bottom: 0;
  word-break: normal;
}

html body pre code,
html body pre tt {
  display: inline;
  max-width: initial;
  padding: 0;
  margin: 0;
  overflow: initial;
  line-height: inherit;
  word-wrap: normal;
  background-color: transparent;
  border: 0;
}

html body pre code:before,
html body pre tt:before,
html body pre code:after,
html body pre tt:after {
  content: normal;
}

html body p,
html body blockquote,
html body ul,
html body ol,
html body dl,
html body pre {
  margin-top: 0;
  margin-bottom: 16px;
}

html body kbd {
  color: #000;
  border: 1px solid #d6d6d6;
  border-bottom: 2px solid #c7c7c7;
  padding: 2px 4px;
  background-color: #f0f0f0;
  border-radius: 3px;
}

@media print {
  html body {
    background-color: #fff;
  }

  html body h1,
  html body h2,
  html body h3,
  html body h4,
  html body h5,
  html body h6 {
    color: #000;
    page-break-after: avoid;
  }

  html body blockquote {
    color: #5c5c5c;
  }

  html body pre {
    page-break-inside: avoid;
  }

  html body table {
    display: table;
  }

  html body img {
    display: block;
    max-width: 100%;
    max-height: 100%;
  }

  html body pre,
  html body code {
    word-wrap: break-word;
    white-space: pre;
  }
}

.markdown-preview {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}

.markdown-preview .pagebreak,
.markdown-preview .newpage {
  page-break-before: always;
}

.markdown-preview pre.line-numbers {
  position: relative;
  padding-left: 3.8em;
  counter-reset: linenumber;
}

.markdown-preview pre.line-numbers > code {
  position: relative;
}

.markdown-preview pre.line-numbers .line-numbers-rows {
  position: absolute;
  pointer-events: none;
  top: 1em;
  font-size: 100%;
  left: 0;
  width: 3em;
  letter-spacing: -1px;
  border-right: 1px solid #999;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.markdown-preview pre.line-numbers .line-numbers-rows > span {
  pointer-events: none;
  display: block;
  counter-increment: linenumber;
}

.markdown-preview pre.line-numbers .line-numbers-rows > span:before {
  content: counter(linenumber);
  color: #999;
  display: block;
  padding-right: 0.8em;
  text-align: right;
}

.markdown-preview .mathjax-exps .MathJax_Display {
  text-align: center !important;
}

.markdown-preview:not([for="preview"]) .code-chunk .btn-group {
  display: none;
}

.markdown-preview:not([for="preview"]) .code-chunk .status {
  display: none;
}

.markdown-preview:not([for="preview"]) .code-chunk .output-div {
  margin-bottom: 16px;
}

.scrollbar-style::-webkit-scrollbar {
  width: 8px;
}

.scrollbar-style::-webkit-scrollbar-track {
  border-radius: 10px;
  background-color: transparent;
}

.scrollbar-style::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background-color: rgba(150, 150, 150, 0.66);
  border: 4px solid rgba(150, 150, 150, 0.66);
  background-clip: content-box;
}

html body[for="html-export"]:not([data-presentation-mode]) {
  position: relative;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
  overflow: auto;
}

html body[for="html-export"]:not([data-presentation-mode]) .markdown-preview {
  position: relative;
  top: 0;
}

@media screen and (min-width: 914px) {
  html body[for="html-export"]:not([data-presentation-mode]) .markdown-preview {
    padding: 2em calc(50% - 457px + 2em);
  }
}

@media screen and (max-width: 914px) {
  html body[for="html-export"]:not([data-presentation-mode]) .markdown-preview {
    padding: 2em;
  }
}

@media screen and (max-width: 450px) {
  html body[for="html-export"]:not([data-presentation-mode]) .markdown-preview {
    font-size: 14px !important;
    padding: 1em;
  }
}

@media print {
  html body[for="html-export"]:not([data-presentation-mode]) #sidebar-toc-btn {
    display: none;
  }
}

html body[for="html-export"]:not([data-presentation-mode]) #sidebar-toc-btn {
  position: fixed;
  bottom: 8px;
  left: 8px;
  font-size: 28px;
  cursor: pointer;
  color: inherit;
  z-index: 99;
  width: 32px;
  text-align: center;
  opacity: 0.4;
}

html
  body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
  #sidebar-toc-btn {
  opacity: 1;
}

html
  body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
  .md-sidebar-toc {
  position: fixed;
  top: 0;
  left: 0;
  width: 300px;
  height: 100%;
  padding: 32px 0 48px 0;
  font-size: 14px;
  box-shadow: 0 0 4px rgba(150, 150, 150, 0.33);
  box-sizing: border-box;
  overflow: auto;
  background-color: inherit;
}

html
  body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
  .md-sidebar-toc::-webkit-scrollbar {
  width: 8px;
}

html
  body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
  .md-sidebar-toc::-webkit-scrollbar-track {
  border-radius: 10px;
  background-color: transparent;
}

html
  body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
  .md-sidebar-toc::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background-color: rgba(150, 150, 150, 0.66);
  border: 4px solid rgba(150, 150, 150, 0.66);
  background-clip: content-box;
}

html
  body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
  .md-sidebar-toc
  a {
  text-decoration: none;
}

html
  body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
  .md-sidebar-toc
  ul {
  padding: 0 1.6em;
  margin-top: 0.8em;
}

html
  body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
  .md-sidebar-toc
  li {
  margin-bottom: 0.8em;
}

html
  body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
  .md-sidebar-toc
  ul {
  list-style-type: none;
}

html
  body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
  .markdown-preview {
  left: 300px;
  width: calc(100% - 300px);
  padding: 2em calc(50% - 457px - 150px);
  margin: 0;
  box-sizing: border-box;
}

@media screen and (max-width: 1274px) {
  html
    body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
    .markdown-preview {
    padding: 2em;
  }
}

@media screen and (max-width: 450px) {
  html
    body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc]
    .markdown-preview {
    width: 100%;
  }
}

html
  body[for="html-export"]:not([data-presentation-mode]):not([html-show-sidebar-toc])
  .markdown-preview {
  left: 50%;
  transform: translateX(-50%);
}

html
  body[for="html-export"]:not([data-presentation-mode]):not([html-show-sidebar-toc])
  .md-sidebar-toc {
  display: none;
}

/* Please visit the URL below for more information: */
/*   https://shd101wyy.github.io/markdown-preview-enhanced/#/customize-css */
</style>