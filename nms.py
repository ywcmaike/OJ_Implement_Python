#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/6/25 上午12:27

# Definition for a binary tree node.

def py_cpu_nms(dets, thresh):
	x1 = dets[:, 0]
	y1 = dets[:, 1]
	x2 = dets[:, 2]
	y2 = dets[:, 3]
	scores = dets[:, 4]
	areas = (x2-x1+1) * (y2-y1+1)
	order = scores.argsort()[::-1]

	keep = []
	while order.size() > 0:
		i = order[0]
		keep.append(i)

		xx1 = np.maximum(x1[i], x1[order[1:]])
		yy1 = np.maximum(y1[i], y1[order[1:]])
		xx2 = np.minimum(x2[i], y2[order[1:]])
		yy2 = np.minimum(y2[i], y2[order[1:]])

		w = np.maximum(0.0, xx2-xx1+1)
		h = np.maximum(0.0, yy2-yy1+1)

		inter = w*h

		ovr = inter / (areas[i] + areas[order[i:]] - inter)
		inds = np.where(ovr <= thresh)[0]

		order = order[inds + 1]

	return keep


# soft-nms
ua = float((tx2 - tx1 + 1) * (ty2 - ty1 + 1) + area - iw * ih)
ov = iw * ih / ua #iou between max box and detection box 
if method == 1: # linear 
	if ov > Nt: weight = 1 - ov 
else:
	weight = 1
elif method == 2: # gaussian 
	weight = np.exp(-(ov * ov)/sigma) 
else: # original NMS 
	if ov > Nt: 
		weight = 0 
	else: 
		weight = 1 
# re-scoring 修改置信度 boxes[pos, 4] = weight*boxes[pos, 4]
著作权归作者所有。商业转载请联系作者获得授权,非商业转载请注明出处。
原文: https://www.cnblogs.com/makefile/p/nms.html © 康行天下

