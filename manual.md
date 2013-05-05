Linux Deepin 应用程序开发手册
==========================

> 王勇 于 2013年夏

* * *

*    [前言](#prelude)
    *    [致战斗在一线的 Linux Deepin 勇士们, 为理想而战！](#for-dream)
    *    [为什么我要写这本书？](#why-i-write-this-book)
    *    [面向的读者人群及读者应该具有怎样的基础?](#reader-need-to-know)
    *    [Linux需要什么样的应用程序？](#what-kind-of-application-is-we-need)
    *    [开发者应该怀着怎样的理念去开发用户喜欢的产品？](#development-concept)
    *    [我们需要怎样的应用开发社区氛围？](#how-to-build-development-community)
  
*    [编码之前的思考](#think-before-coding)
    *    [怎样一步一步构建Linux应用程序？](#build-application-step-by-step)
    *    [开发应用程序都需要掌握哪些基本技术？](#what-technology-we-need)
    *    [构建应用程序的基本技术](#basic-technology)
    *    [构建应用程序的高级技术](#advanced-technology)
    *    [写补丁的规则](#how-to-write-patch)
    *    [编写代码的准则](#the-rule-of-coding)
    *    [为什么选择 PyGTK+ 作为应用程序开发基础？](#why-choose-pygtk)
    *    [关于 Python/PyGTK+ 的错误认识](#misconceptions-about-python/pygtk)
    *    [Python代码编写规范](#python-coding-specification)
  
*    [应用开发基础技术](#application-development-technology)
    *    [GTK+陷阱与技巧](#gtk-trick)
    *    [编写 Python C 扩展](#build-c-extension)
    *    [更多技术...](#more-technology)
	
*    [Deepin-UI](#deepin-ui)
    *    [Deepin-UI 诞生的故事](#how-deepin-ui-born)
    *    [为什么需要 Deepin-UI?](#why-we-need-deepin-ui)
    *    [Deepin-UI 原理](#principle-of-deepin-ui)
    *    [Deepin-UI hello world!](#deepin-ui-hello-world)
    *    [Deepin-UI 简单控件使用](#usage-of-simple-widget)
    *    [Deepin-UI 高级控件使用](#usage-of-advanced-widget)
    *    [Deepin-UI 应用开发实例](#application-development-example)
	
*    [编写控件的艺术](#the-art-of-building-widget)
    *    [控件的重要性!](#the-importance-of-widget)
    *    [控件编写的基本原理](#the-principle-of-building-widget)
    *    [控件的构思到实现](#from-conception-to-realization)
    *    [控件编写实例](#widget-building-example)
	
* * *

<h2 id="prelude">前言</h2>

<h3 id="for-dream">致战斗在一线的 Linux Deepin 勇士们, 为理想而战！</h3>

<h3 id="why-i-write-this-book">为什么我要写这本书?</h3>
> Linux 从1991年诞生到现在的20多年已经深入了我们生活的方方面面，
从个人电脑到超级计算机， 从电视机顶盒到我们天天把玩的手机、平板，
甚至在各种毫不起眼的地方（地铁， 公交车站， 售货机， 电子广告牌等）都在运行着Linux。

> 全世界的黑客每天都在通过自己过人的天赋和勤奋向世界证明，
即使我们分散在世界各地， 即使我们互不认识， 我们依然能通过无私和正能量建造世界上最伟大的操作系统！

<h2 id="deepin-ui">Deepin-UI</h2>

<h3 id="how-deepin-ui-born">Deepin-UI诞生的故事</h3>

