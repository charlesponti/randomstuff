"use client";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import type { Task } from "@ponti/utils";
import { Calendar, Hash, Tag } from "lucide-react";
import React, { useState } from "react";

import { parseInput } from "@/lib/text.tools.ts";

const SmartTaskInput = () => {
	const [inputValue, setInputValue] = useState("");
	const [task, setTask] = useState<Task>({
		title: "",
		dueDate: null,
		category: "",
		labels: [],
	});

	const handleInputChange = (e) => {
		const value = e.target.value;
		setInputValue(value);
		setTask(parseInput(value));
	};

	const formatDate = (date) => {
		if (!date) return "";
		return date.toLocaleDateString("en-US", {
			weekday: "long",
			month: "short",
			day: "numeric",
		});
	};

	return (
		<div className="flex flex-col items-center justify-center pt-4">
			<Card className="container max-w-2xl">
				<CardContent className="pt-6">
					<div className="space-y-4">
						<Input
							value={inputValue}
							onChange={handleInputChange}
							placeholder="Add task (try: Buy groceries next Friday #shopping @errands)"
							className="w-full text-lg"
						/>

						{(task.title ||
							task.dueDate ||
							task.category ||
							task.labels.length > 0) && (
							<div className="space-y-3 p-4 bg-gray-50 rounded-lg">
								{task.title && <div className="font-medium">{task.title}</div>}

								<div className="flex flex-wrap gap-2">
									{task.dueDate && (
										<Badge
											variant="outline"
											className="flex items-center gap-1"
										>
											<Calendar className="w-3 h-3" />
											{formatDate(task.dueDate)}
										</Badge>
									)}

									{task.category && (
										<Badge
											variant="secondary"
											className="flex items-center gap-1"
										>
											<Hash className="w-3 h-3" />
											{task.category}
										</Badge>
									)}

									{task.labels.map((label) => (
										<Badge key={label} className="flex items-center gap-1">
											<Tag className="w-3 h-3" />
											{label}
										</Badge>
									))}
								</div>
							</div>
						)}
					</div>
				</CardContent>
			</Card>
		</div>
	);
};

export default SmartTaskInput;
